from argonaut.tests import *

class TestBlogController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='blog', action='index'))
        # Test response...
