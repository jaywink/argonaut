import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from argonaut.lib.base import BaseController, render
import argonaut.lib.helpers as h

log = logging.getLogger(__name__)

class PageController(BaseController):

    def show(self,id):
        try:
            page_id = h.page.get_id_by_url_param(id)
        except:
            try:
                page_id = h.page.get_id_by_type_param(id)
            except:
                abort(404)
        try:
            return render('/pages/'+id+'.mako', extra_vars={'page_id':page_id})
        except Exception, e:
            abort(404)
