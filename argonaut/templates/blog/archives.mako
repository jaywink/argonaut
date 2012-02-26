<%inherit file="/base.mako"/>\

<%def name="title()">\
    ${h.page.get_title(page_id)}
</%def>

<%def name="buildrow(post, odd=True)">
    %if odd:
        <tr class="odd">
    %else:
        <tr class="even">
    % endif
        <td valign="top">
            ${h.link_to(
                post.id,
                h.url(
                    'blog_post',
                    id=post.id,
                    subject=h.urlify(post.subject)
                )
            )}
        </td>
        <td valign="top">
            ${post.subject}
        </td>
        <td valign="top">${post.posted.strftime('%c')}</td>
        </tr>
</%def>

## heading
<h1>${h.page.get_name(page_id)}</h1>

## filter
<%include file="/forms/filter.mako"/>\

## paginator
% if len(c.paginator):
    <p>${ c.paginator.pager('$link_first $link_previous $first_item to $last_item of $item_count $link_next $link_last') }</p>
    <table class="paginator"><tr><th>Post ID</th><th>Post Title</th><th>Posted</th></tr>
    <% counter=0 %>
    % for item in c.paginator:
        ${buildrow(item, counter%2)}
        <% counter += 1 %>
    % endfor
    </table>
    <p>${ c.paginator.pager('~2~') }</p>
% else:
    <p>
        No posts.
    </p>
% endif



