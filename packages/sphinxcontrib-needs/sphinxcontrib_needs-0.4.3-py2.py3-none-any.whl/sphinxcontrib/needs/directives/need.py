# -*- coding: utf-8 -*-
import hashlib
import re

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive
from sphinx.errors import SphinxError
from sphinx.addnodes import desc_signature, desc_name

from pkg_resources import parse_version
import sphinx
from sphinx.util.nodes import make_refnode

from sphinxcontrib.needs.api import add_need

from sphinxcontrib.needs.roles.need_incoming import Need_incoming
from sphinxcontrib.needs.roles.need_outgoing import Need_outgoing
from sphinxcontrib.needs.functions import resolve_dynamic_values, find_and_replace_node_content
from sphinxcontrib.needs.api.exceptions import NeedsInvalidException


sphinx_version = sphinx.__version__
if parse_version(sphinx_version) >= parse_version("1.6"):
    from sphinx.util import logging
else:
    import logging
logger = logging.getLogger(__name__)

NON_BREAKING_SPACE = re.compile('\xa0+')


class Need(nodes.General, nodes.Element):
    """
    Node for containing a complete need.
    Node structure:

    - need
      - headline container
      - meta container ()
      - content container

    As the content container gets rendered RST input, this must already be created during
    node handling and can not be done later during event handling.
    Reason: nested_parse_with_titles() needs self.state, which is available only during node handling.

    headline and content container get added later during event handling (process_need_nodes()).
    """
    child_text_separator = "\n"
    pass


class NeedDirective(Directive):
    """
    Collects mainly all needed need-information and renders its rst-based content.

    It only creates a basic node-structure to support later manipulation.
    """
    # this enables content in the directive
    has_content = True

    required_arguments = 1
    optional_arguments = 0
    option_spec = {'id': directives.unchanged_required,
                   'status': directives.unchanged_required,
                   'tags': directives.unchanged_required,
                   'links': directives.unchanged_required,
                   'collapse': directives.unchanged_required,
                   'hide': directives.flag,
                   'hide_tags': directives.flag,
                   'hide_status': directives.flag,
                   'hide_links': directives.flag,
                   'title_from_content': directives.flag,
                   'style': directives.unchanged_required}

    # add configured link types

    final_argument_whitespace = True

    def __init__(self, *args, **kw):
        super(NeedDirective, self).__init__(*args, **kw)
        self.log = logging.getLogger(__name__)
        self.full_title = self._get_full_title()

    def run(self):
        #############################################################################################
        # Get environment
        #############################################################################################
        env = self.env

        # ToDo: Keep this in directive!!!
        collapse = str(self.options.get("collapse", ""))
        if isinstance(collapse, str) and len(collapse) > 0:
            if collapse.upper() in ["TRUE", 1, "YES"]:
                collapse = True
            elif collapse.upper() in ["FALSE", 0, "NO"]:
                collapse = False
            else:
                raise Exception("collapse attribute must be true or false")
        else:
            collapse = getattr(env.app.config, "needs_collapse_details", True)

        hide = True if "hide" in self.options.keys() else False
        hide_tags = True if "hide_tags" in self.options.keys() else False
        hide_status = True if "hide_status" in self.options.keys() else False

        id = self.options.get("id", None)
        content = "\n".join(self.content)
        status = self.options.get("status", None)
        tags = self.options.get("tags", '')
        style = self.options.get("style", '')

        need_extra_options = {}
        for extra_link in env.config.needs_extra_links:
            need_extra_options[extra_link['option']] = self.options.get(extra_link['option'], '')

        for extra_option in env.config.needs_extra_options.keys():
            need_extra_options[extra_option] = self.options.get(extra_option, '')

        return add_need(env.app, self.state, self.docname, self.lineno,
                        need_type=self.name, title=self.trimmed_title, id=id, content=content,
                        status=status, tags=tags,
                        hide=hide, hide_tags=hide_tags, hide_status=hide_status,
                        collapse=collapse, style=style, **need_extra_options)

    def read_in_links(self, name):
        # Get links
        links_string = self.options.get(name, [])
        links = []
        if len(links_string) > 0:
            # links = [link.strip() for link in re.split(";|,", links) if not link.isspace()]
            for link in re.split(";|,", links_string):
                if not link.isspace():
                    links.append(link.strip())
                else:
                    logger.warning('Grubby link definition found in need {}. '
                                   'Defined link contains spaces only.'.format(id))

            # This may have cut also dynamic function strings, as they can contain , as well.
            # So let put them together again
            # ToDo: There may be a smart regex for the splitting. This would avoid this mess of code...
        return _fix_list_dyn_func(links)

    def make_hashed_id(self, type_prefix, id_length):
        hashable_content = self.full_title or '\n'.join(self.content)
        return "%s%s" % (type_prefix,
                         hashlib.sha1(hashable_content.encode("UTF-8"))
                         .hexdigest()
                         .upper()[:id_length])

    @property
    def env(self):
        return self.state.document.settings.env

    @property
    def title_from_content(self):
        return ('title_from_content' in self.options or
                self.env.config.needs_title_from_content)

    @property
    def docname(self):
        return self.state.document.settings.env.docname

    @property
    def trimmed_title(self):
        title = self.full_title
        max_length = self.max_title_length
        if max_length == -1 or len(title) <= max_length:
            return title
        elif max_length <= 3:
            return title[:self.max_title_length]
        else:
            return title[:self.max_title_length - 3] + '...'

    @property
    def max_title_length(self):
        return self.state.document.settings.env.config.needs_max_title_length

    # ToDo. Keep this in directive
    def _get_full_title(self):
        """
        Determines the title for the need in order of precedence:
        directive argument, first sentence of requirement (if
        `:title_from_content:` was set, and '' if no title is to be derived."""
        if len(self.arguments) > 0:  # a title was passed
            if 'title_from_content' in self.options:
                self.log.warning(
                    'Needs: need "{}" has :title_from_content: set, '
                    'but a title was provided. (see file {})'
                        .format(self.arguments[0], self.docname)
                )
            return self.arguments[0]
        elif self.title_from_content:
            first_sentence = ' '.join(self.content).split('.', 1)[0]
            if not first_sentence:
                raise NeedsInvalidException(':title_from_content: set, but '
                                            'no content provided. '
                                            '(Line {} of file {}'
                                            .format(self.lineno, self.docname))
            return first_sentence
        else:
            return ''


def get_sections_and_signature(need_info):
    """Gets the hierarchy of the section nodes as a list starting at the
    section of the current need and then its parent sections"""
    sections = []
    signature = None
    current_node = need_info['target_node']
    while current_node:
        if isinstance(current_node, nodes.section):
            title = current_node.children[0].astext()
            # If using auto-section numbering, then Sphinx inserts
            # multiple non-breaking space unicode characters into the title
            # we'll replace those with a simple space to make them easier to
            # use in filters
            title = NON_BREAKING_SPACE.sub(' ', title)
            sections.append(title)

        # Checking for a signature defined "above" the need.
        # Used and set normally by directives like automodule.
        # Only check as long as we haven't found a signature
        if signature is None and current_node.parent is not None and current_node.parent.children is not None:
            for sibling in current_node.parent.children:
                # We want to check only "above" current node, so no need to check sibling after current_node.
                if sibling == current_node:
                    break
                if isinstance(sibling, desc_signature):
                    # Check the child of the found signature for the text content/node.
                    for desc_child in sibling.children:
                        if isinstance(desc_child, desc_name) and \
                                isinstance(desc_child.children[0], nodes.Text):
                            signature = desc_child.children[0]
                if signature is not None:
                    break

        current_node = getattr(current_node, 'parent', None)
    return sections, signature


def purge_needs(app, env, docname):
    """
    Gets executed, if a doc file needs to be purged/ read in again.
    So this code delete all found needs for the given docname.
    """
    if not hasattr(env, 'needs_all_needs'):
        return
    env.needs_all_needs = {key: need for key, need in env.needs_all_needs.items() if need['docname'] != docname}


def add_sections(app, doctree, fromdocname):
    """Add section titles to the needs as additional attributes that can
    be used in tables and filters"""
    needs = getattr(app.builder.env, 'needs_all_needs', {})
    for key, need_info in needs.items():
        sections, signature = get_sections_and_signature(need_info)
        need_info['sections'] = sections
        need_info['section_name'] = sections[0] if sections else ""
        need_info['signature'] = signature if signature else ""


def process_need_nodes(app, doctree, fromdocname):
    """
    Event handler to add title meta data (status, tags, links, ...) information to the Need node.

    :param app:
    :param doctree:
    :param fromdocname:
    :return:
    """
    if not app.config.needs_include_needs:
        for node in doctree.traverse(Need):
            node.parent.remove(node)
        return

    env = app.builder.env

    # If no needs were defined, we do not need to do anything
    if not hasattr(env, "needs_all_needs"):
        return

    needs = env.needs_all_needs

    # Call dynamic functions and replace related note data with their return values
    resolve_dynamic_values(env)

    # Create back links of common links and extra links
    for links in env.config.needs_extra_links:
        create_back_links(env, links['option'])

    for node_need in doctree.traverse(Need):
        need_id = node_need.attributes["ids"][0]
        need_data = needs[need_id]

        find_and_replace_node_content(node_need, env, need_data)
        from sphinxcontrib.needs.functions.functions import check_and_get_content
        for index, attribute in enumerate(node_need.attributes['classes']):
            node_need.attributes['classes'][index] = check_and_get_content(attribute, need_data, env)


        node_headline = construct_headline(need_data, app)
        node_meta = construct_meta(need_data, env)

        # Collapse check
        if need_data["collapse"] and "HTML" in app.builder.name.upper():
            # HEADER
            node_need_toogle_container = nodes.container(classes=['toggle'])
            node_need_toogle_head_container = nodes.container(classes=['header'])
            node_need_toogle_head_container += node_headline.children

            node_need_toogle_container.append(node_need_toogle_head_container)

            # Only add node_meta(line_block), if it has lines in it
            # Otherwise the pdf/latex build will claim about an empty line_block.
            if node_meta.children:
                node_need_toogle_container.append(node_meta)

            node_need.insert(0, node_need_toogle_container)
        else:
            node_meta.insert(0, node_headline)
            node_need.insert(0, node_meta)


def create_back_links(env, option):
    """
    Create back-links in all found needs.
    But do this only once, as all needs are already collected and this sorting is for all
    needs and not only for the ones of the current document.

    :param env: sphinx enviroment
    :return: None
    """
    option_back = '{}_back'.format(option)
    if env.needs_workflow['backlink_creation_{}'.format(option)]:
        return

    needs = env.needs_all_needs
    for key, need in needs.items():
        for link in need[option]:
            link_main = link.split('.')[0]
            try:
                link_part = link.split('.')[1]
            except IndexError:
                link_part = None

            if link_main in needs:
                if key not in needs[link_main][option_back]:
                    needs[link_main][option_back].append(key)

                # Handling of links to need_parts inside a need
                if link_part is not None:
                    if link_part in needs[link_main]['parts']:
                        if option_back not in needs[link_main]['parts'][link_part].keys():
                            needs[link_main]['parts'][link_part][option_back] = []
                        needs[link_main]['parts'][link_part][option_back].append(key)

    env.needs_workflow['backlink_creation_{}'.format(option)] = True


def construct_headline(need_data, app):
    """
    Constructs the node-structure for the headline/title container
    :param need_data: need_info container
    :return: node
    """
    # need title calculation
    title_type = '{}: '.format(need_data["type_name"])
    title_headline = need_data["title"]
    title_id = "{}".format(need_data["id"])
    title_spacer = " "

    # need title
    node_type = nodes.inline(title_type, title_type, classes=["needs-type"])
    node_title = nodes.inline(title_headline, title_headline, classes=["needs-title"])

    nodes_id = nodes.inline(classes=["needs-id"])

    nodes_id_text = nodes.Text(title_id, title_id)
    id_ref = make_refnode(app.builder,
                          fromdocname=need_data['docname'],
                          todocname=need_data['docname'],
                          targetid=need_data['id'],
                          child=nodes_id_text.deepcopy(),
                          title=title_id)
    nodes_id += id_ref

    node_spacer = nodes.inline(title_spacer, title_spacer, classes=["needs-spacer"])

    headline_line = nodes.line(classes=["headline"])
    headline_line.append(node_type)
    headline_line.append(node_spacer)
    headline_line.append(node_title)
    headline_line.append(node_spacer)
    headline_line.append(nodes_id)

    return headline_line


def construct_meta(need_data, env):
    """
    Constructs the node-structure for the status container
    :param need_data: need_info container
    :return: node
    """

    hide_options = env.config.needs_hide_options
    if not isinstance(hide_options, list):
        raise SphinxError('Config parameter needs_hide_options must be of type list')

    node_meta = nodes.line_block(classes=['needs_meta'])
    # need parameters
    param_status = "status: "
    param_tags = "tags: "
    param_style = "style: "

    if need_data["status"] is not None and 'status' not in hide_options:
        status_line = nodes.line(classes=['status'])
        # node_status = nodes.line(param_status, param_status, classes=['status'])
        node_status = nodes.inline(param_status, param_status, classes=['status'])
        status_line.append(node_status)
        status_line.append(nodes.inline(need_data["status"], need_data["status"],
                                        classes=["needs-status", str(need_data['status'])]))
        node_meta.append(status_line)

    if need_data["tags"] and 'tags' not in hide_options:
        tag_line = nodes.line(classes=['tags'])
        # node_tags = nodes.line(param_tags, param_tags, classes=['tags'])
        node_tags = nodes.inline(param_tags, param_tags, classes=['tags'])
        tag_line.append(node_tags)
        for tag in need_data['tags']:
            # node_tags.append(nodes.inline(tag, tag, classes=["needs-tag", str(tag)]))
            # node_tags.append(nodes.inline(' ', ' '))
            tag_line.append(nodes.inline(tag, tag, classes=["needs-tag", str(tag)]))
            tag_line.append(nodes.inline(' ', ' '))
        node_meta.append(tag_line)

    # Links incoming
    for link_type in env.config.needs_extra_links:
        link_back = '{}_back'.format(link_type['option'])
        if need_data[link_back] and link_back not in hide_options:
            node_incoming_line = nodes.line(classes=[link_type['option'], 'incoming'])
            prefix = "{}: ".format(link_type['incoming'])
            node_incoming_prefix = nodes.inline(prefix, prefix)
            node_incoming_line.append(node_incoming_prefix)
            node_incoming_links = Need_incoming(reftarget=need_data['id'], link_type=link_back)
            node_incoming_links.append(nodes.inline(need_data['id'], need_data['id']))
            node_incoming_line.append(node_incoming_links)
            node_meta.append(node_incoming_line)

    # Links outgoing
    for link_type in env.config.needs_extra_links:
        link = '{}'.format(link_type['option'])
        if need_data[link] and link not in hide_options:
            node_outgoing_line = nodes.line(classes=[link_type['option'], 'outgoing'])
            prefix = "{}: ".format(link_type['outgoing'])
            node_outgoing_prefix = nodes.inline(prefix, prefix)
            node_outgoing_line.append(node_outgoing_prefix)
            node_outgoing_links = Need_outgoing(reftarget=need_data['id'], link_type=link)
            node_outgoing_links.append(nodes.inline(need_data['id'], need_data['id']))
            node_outgoing_line.append(node_outgoing_links)
            node_meta.append(node_outgoing_line)

    if need_data["style"] is not None and 'style' not in hide_options and len(need_data["style"]) > 0:
        style_line = nodes.line(classes=['style'])
        node_status = nodes.inline(param_style, param_style, classes=['style'])
        style_line.append(node_status)
        style_line.append(nodes.inline(need_data["style"], need_data["style"],
                                       classes=["needs-style", str(need_data['style'])]))
        node_meta.append(style_line)

    extra_options = getattr(env.config, 'needs_extra_options', {})
    node_extra_options = []
    for key, value in extra_options.items():
        if key in hide_options:
            continue
        param_data = need_data[key]
        if (param_data is None or not param_data) and param_data != 0:
            continue
        param_option = '{}: '.format(key)
        option_line = nodes.line(classes=['extra_option'])
        option_line.append(nodes.inline(param_option, param_option, classes=['extra_option']))
        option_line.append(nodes.inline(param_data, param_data,
                                        classes=["needs-extra-option", str(key)]))
        node_extra_options.append(option_line)

    node_meta += node_extra_options

    global_options = getattr(env.config, 'needs_global_options', {})
    node_global_options = []
    link_types = [x['option'] for x in env.config.needs_extra_links]
    for key, value in global_options.items():
        # If a global option got locally overwritten, it must already part of extra_options.
        # In this skipp output, as this is done during extra_option handling
        # Also if it is part of link_types, the handling is already done.
        # So skip in all of these cases
        if key in extra_options or key in hide_options or key in link_types:
            continue

        param_data = need_data[key]
        if param_data is None or not param_data:
            continue
        param_option = '{}: '.format(key)
        global_option_line = nodes.line(classes=['global_option'])
        global_option_line.append(nodes.inline(param_option, param_option, classes=['global_option']))
        global_option_line.append(nodes.inline(param_data, param_data,
                                               classes=["needs-global-option", str(key)]))
        node_global_options.append(global_option_line)

    node_meta += node_global_options

    return node_meta


def _fix_list_dyn_func(list):
    """
    This searches a list for dynamic function fragments, which may have been cut by generic searches for ",|;".

    Example:
    `link_a, [[copy('links', need_id)]]` this will be splitted in list of 3 parts:

    #. link_a
    #. [[copy('links'
    #. need_id)]]

    This function fixes the above list to the following:

    #. link_a
    #. [[copy('links', need_id)]]

    :param list: list which may contain splitted function calls
    :return: list of fixed elements
    """
    open_func_string = False
    new_list = []
    for element in list:
        if '[[' in element:
            open_func_string = True
            new_link = [element]
        elif ']]' in element:
            new_link.append(element)
            open_func_string = False
            element = ",".join(new_link)
            new_list.append(element)
        elif open_func_string:
            new_link.append(element)
        else:
            new_list.append(element)
    return new_list


#####################
# Visitor functions #
#####################
# Used for builders like html or latex to tell them, what do, if they stumble on a Need-Node in the doctree.
# Normally nothing needs to be done, as all needed output-configuration is done in the child-nodes of the detected
# Need-Node.


def html_visit(self, node):
    """
    Visitor method for Need-node of builder 'html'.
    Does only wrap the Need-content into an extra <div> with class=need
    """
    self.body.append(self.starttag(node, 'div', '', CLASS='need'))


def html_depart(self, node):
    self.body.append('</div>')


def latex_visit(self, node):
    pass


def latex_depart(self, node):
    pass
