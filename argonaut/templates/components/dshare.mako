
<%def name="button(post_id, url=None, title=None)">\
	<img style="cursor:pointer;" src="http://iliketoast.net/img/diasporaWebBadge80x15_3.png" border="0" onClick="dshare${post_id}();">\
	<script type="text/javascript">\
		function dshare${post_id}() {
			% if url:
				var url = "${url}";
			% else:
				var url = window.location.href;
			% endif
			% if title:
				var title = "${title}";
			% else:
				var title = document.title;
			% endif
			var txt = '';
			if (window.getSelection) { 
				txt = window.getSelection(); 
			} else if (window.document.getSelection) { 
				txt = window.document.getSelection(); 
			} else if (window.document.selection) { 
				txt = window.document.selection.createRange().text; 
			}
			window.open('http://iliketoast.net/dshare.html?url='+encodeURIComponent(url)+'&title='+encodeURIComponent(title)+'&notes='+encodeURIComponent(txt),'dshare','location=no,links=no,scrollbars=no,toolbar=no,width=620,height=400');
			return false;
		}
	</script>\
</%def>


