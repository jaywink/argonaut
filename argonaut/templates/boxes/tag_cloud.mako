<p>
<div class="no_overflow">
<%
    tags = h.tag_post.get_tag_counts(True)
    counter = 0
    for tag in tags:
        context.write(' <a href="'+h.url(controller='tag', action='show', id=tag.name)+'"><font size="'+str(tag.count_1)+'">'+tag.name+'</font></a>')
        counter += 1
        if counter > 10:
            break
%>
</div>
</p>
