import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from argonaut.lib.base import BaseController, render

from repoze.what.predicates import not_anonymous, has_permission
from repoze.what.plugins.pylonshq import ActionProtector

log = logging.getLogger(__name__)

class AdminController(BaseController):

    def index(self):
        return "Index"
