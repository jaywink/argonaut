<%inherit file="/base.mako"/>\
<%namespace name="editor" file="/forms/editor.mako" />

<%def name="title()">\
    % if c.post is None:
        ${h.page.generate_title('Write new post')}
    % else:
        ${h.page.generate_title('Edit post: '+c.post.subject)}
    % endif
</%def>

## header
% if c.post is None:
    <h1>Write new post</h1>
% else:
    <h1>Edit post: ${c.post.subject}</h1>
% endif

## editor
${editor.editor_form(c.post)}






