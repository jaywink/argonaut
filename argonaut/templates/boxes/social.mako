<p>
<%
    for social in h.social.get_active():
        context.write('<a href="'+social.url+'" target="_blanc">')
        media = h.media.get(social.media_id)
        context.write('<img src="'+media.url+'" border="0" style="padding-right:1px; padding-bottom:1px;" alt="'+media.name+'" title="'+social.name+'">')
        context.write('</a>')
%> 
</p>
