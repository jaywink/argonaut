<%inherit file="/base.mako"/>\
<%namespace name="tags_list" file="/blog/tags_list.mako" />

<%def name="title()">\
    ${h.page.get_title(page_id)}
</%def>

## heading
<h1>${h.page.get_name(page_id)}</h1>

${tags_list.list_as_links(tags)}
