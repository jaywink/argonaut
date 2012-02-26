import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from argonaut.lib.base import BaseController, render
import argonaut.lib.helpers as h

import webhelpers.paginate as paginate

log = logging.getLogger(__name__)

class TagController(BaseController):

    def show_all(self):
        tags = h.tag_post.get_tag_counts()
        page_id = int(h.page.get_page_id_with_type('tags'))
        return render('/blog/tags.mako', extra_vars={'tags':tags, 'page_id':page_id})

    def show(self,id):
        
        posts = h.post.get_by_tag_name(id)
        if posts is None:
            abort(404)
        c.paginator = paginate.Page(
            posts,
            page=int(request.params.get('page', 1)),
            items_per_page = 20,
            )
        page_id = int(h.page.get_page_id_with_type('tags'))
        return render('/blog/posts_tag.mako', extra_vars={'page_id':page_id, 'tag':id})
