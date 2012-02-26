import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from argonaut.lib.base import BaseController, render
import argonaut.lib.helpers as h

log = logging.getLogger(__name__)

class LandingController(BaseController):
    
    def first_page(self):
        # redirects to the first page
        first_page = h.page.get_first()
        if first_page:
            redirect(h.resolve_page_url(first_page.id))
        else:
            abort(404)
 
