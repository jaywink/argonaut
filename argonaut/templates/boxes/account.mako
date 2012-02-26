<p>
<%
    logged = h.authentication.get_logged_user()
%>
%if not logged:
    <%include file="/forms/login.mako"/>\
%else:
    <%
        identity = h.authentication.get_logged_identity()
        context.write(identity['repoze.who.userid']+' [<a href="'+h.url(controller='account', action='logout')+'">log out</a>]')
        context.write('<p>')
        if h.authentication.has_permission('Write post'):
            context.write('<a href="'+h.url(controller='blog', action='write')+'">Write a new post</a>')
        context.write('</p>')
    %>
%endif
</p>
