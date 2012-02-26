<%def name="post(post,page)">\
    <%namespace name="share" file="/components/add2any.mako" />
    <%namespace name="dshare" file="/components/dshare.mako" />
    <%namespace name="comment" file="/forms/comment.mako" />
    <script type="text/javascript">
        var post_${post.id} = new Post();
        $(document).ready(function() {
            post_${post.id}.init(${post.id},'${page}');
        });
    </script>
    <%
        c.counter_post_on_page += 1
        title = h.escape(h.page.generate_title(post.subject))
        link = h.config.get('site_url')+h.escape(h.url('blog_post', id=post.id, subject=h.urlify(post.subject)))
        ## posted
        context.write('<p><div id="post_posted">#'+str(post.id)+' posted on '+post.posted.strftime('%c')+'</div>')
        ## add edit button if logged in authorized user
        if h.authentication.get_logged_user():
            if h.authentication.has_permission('Write post'):
                context.write('<div style="float:right;"><a href="'+h.url(controller='blog', action='write', id=post.id)+'">[edit]</a></div>')
        context.write('</p>')
    %>
    <script type="text/javascript">
        var title_${post.id} = "${title}";
        var link_${post.id} = "${link}";
    </script>
    <h1><a href="${h.url('blog_post', id=post.id, subject=h.urlify(post.subject))}">${post.subject}</a></h1>
    <%
        context.write('<div id="post_body"><p>'+post.body+'</p></div>')
        tags = h.tag_post.get_tags(post.id)
        if len(tags) > 0:
            context.write('<div id="post_tags"><p>[ ')
            first = True
            for tag in tags:
                html = '<a href="'+h.url(controller='tag', action='show', id=tag.name)+'">'+tag.name+'</a>'
                if first:
                    context.write(html)
                else:
                    context.write(' // '+html)
                first = False
            context.write(' ]</p></div>')
    %>  
    <div id="share_button">
        ${share.button(title,link)}
        ${dshare.button(post.id,link,title)}
    </div>
    <%
        ## show comment form and comments if commenting is not disabled
        if h.config.get('comments_enabled') == 'true':
            comment.comment_form(post)
        context.write('<div id="post_between"><p><br></p></div>')
    %>
</%def>

<%def name="comments()">\
    ...
</%def>
