## -*- coding: utf-8 -*-

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <title>${self.title()}</title>
    ${self.head()}
</head>
<body>
    ${self.custom_javascript()}
    <div id="header">
    ${self.header()}
    ${self.heading()}
    ${self.breadcrumbs()}
     <div id="menu">
      <ul id="nav">
       ${self.tabs()}
      </ul>
     </div>
    </div>
    <div id="content">
    <div id="right">
    ${self.flash()}
    ${next.body()}
    </div>
        
    <div id="left">
        ${next.menu()}
        ${self.boxes()}
        ${self.copyright()}
##${self.footer()}
    </div>
    </div>
</body>
</html>

<%def name="title()">\
    ${h.config.get('site_title')}
</%def>
<%def name="head()">\
    ${h.stylesheet_link(h.url('/css/main.css'), media='screen')}
    ${h.javascript_link('/js/jquery-1.4.2.min.js')}
    ${h.javascript_link('/js/post.js')}
    ${h.auto_discovery_link(h.url(controller='feed', action='posts'))}
</%def>
<%def name="custom_javascript()">\
    <%include file="/components/custom_javascript.mako"/>\
</%def>
<%def name="header()">\
    <a name="top"></a>
</%def>
<%def name="tabs()">\
    <%
        for page in h.page.get_active():
			if not page.parent_id:
				context.write('<li><a href="'+h.resolve_page_url(page.id)+'">'+page.name+'</a></li>')
    %>
</%def>
<%def name="boxes()">\
    <%
        for box in h.boxes.get_all():
            box_type = h.box.get(box.id)
            context.write('<div class="box"><h2>'+box_type.name+'</h2>')
            context.write(h.render(box_type.template))
            context.write('</div>')
    %>
</%def>
<%def name="menu()"></%def>
<%def name="heading()">\
    ${h.image('/site_logo.gif', 'Argonaut', id='site_logo')}
    <h1><div id="site_header">${h.link_to(h.config.get('site_title'),h.config.get('site_url'))}</div></h1>
</%def>
<%def name="breadcrumbs()"></%def>
<%def name="footer()">\
    <p><a href="#top">Top ^</a></p>
</%def>
<%def name="copyright()">\
    <div class="box"><div style="font-size: 0.8em;">Powered by <a href="http://pypi.python.org/pypi/Argonaut">Argonaut</a> ${h.version.VERSION}</div></div>
</%def>
<%def name="flash()">
    % if session.has_key('flash'):
        <div id="flash"><p>${session.get('flash')}</p></div>
        <%
            del session['flash']
            session.save()
        %>
    % endif
</%def>
