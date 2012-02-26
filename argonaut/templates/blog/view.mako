<%inherit file="/base.mako"/>\
<%namespace name="p" file="/blog/post.mako" />

<%def name="title()">\
    % if c.posts:
        ${h.page.get_title(page_id)}
    % else:
        ${h.page.generate_title(c.post.subject)}
    % endif
</%def>

<%
    c.counter_post_on_page = 0
%>

% if c.posts:
    % for post in c.posts:
        ${p.post(post, page)}
    % endfor
% elif c.post:
    ${p.post(c.post, page)}
% else:
    There are no posts yet.
% endif






