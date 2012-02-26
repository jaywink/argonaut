<%def name="comment_form(post)">
    <div id="comment_main">
        <p></p>
        <div class="post_comment" id="post_comment_${post.id}" name="post_comment_${post.id}">
            <h2>Write a comment</h2><br>
            ${h.form(h.url(controller='comment', action='submit'), method='post')}
            <table>
            <tr><td>Author (optional):</td><td>${h.text('author')}</td></tr>
            <tr><td>Website (optional):</td><td>${h.text('author_website')}</td></tr>
            </table>
            <table>
            <tr><td style="width:75%;">${h.textarea('body', rows=8)}</td>
            <td style="width:25%; opacity:0.5; padding:10px;">No HTML codes allowed. URL's will automatically be converted to links.</td></tr>
            </table>
            ${h.hidden('post_id', value=post.id)}
            ${h.hidden('antiSpam', id='antiSpam', value='Please do not alter')}
            <p>${h.submit('comment_submit', 'Submit', disabled='true')}</p>
            ${h.end_form()}<br>
        </div>
        <div class="comments">
            <a name="comments">
            <h2>Comments (<a style="cursor:pointer;" class="comment_form_expand_${post.id}">post a comment</a>)</h2>
            <div id="comments_holder_${post.id}" name="comments_holder_${post.id}">
            <!--
                Comments inserted here via javascript and ajax  
            -->
            <%
                comment_count = h.comment.get_post_comment_count(post.id)
            %>
            % if page != 'view' and comment_count > 0:
                <p><a style="cursor:pointer;" class="comments_show_${post.id}">[click to see ${str(comment_count)} comments]</a></p>
            % endif
            </div>
            <div id="ajax_loading_${post.id}">
                <img src="/img/ajax-loader.gif">
            </div>
        </div>
    </div>
</%def>

<%def name="link_to_comments(post_id)">
    <div id="comment_main">
        <p>
        <%
            comment_count = h.comment.get_post_comment_count(post_id)
            context.write('<div id="go_to_post_link" onclick="go_to_post_'+str(post_id)+'();">[share post or view/post comments ('+str(comment_count)+')]</div>')
        %>
        <script language="javascript">
            function go_to_post_${post_id}() {
                window.location.href = "/blog/view/${post_id}#comments";
            }
        </script>
        </p>
    </div>

</%def>
