## list tags

<%def name="list_as_links(tags)">
    <%
        for tag in tags:
            context.write(' <a href="'+h.url(controller='tag', action='show', id=tag.name)+'"><font size="'+str(tag.count_1)+'">'+tag.name+'</font></a>')
    %>
</%def>

<%def name="list_as_links_for_editor(tags)">
    <%
        for tag in tags:
            context.write(' <a href="#" onClick="toggleTag(document.getElementById(\'tags\').value, \''+tag.name+'\');"><span id="tag_'+tag.name+'"><font size="'+str(tag.count_1)+'">'+tag.name+'</font></span></a>')
    %>
</%def>
