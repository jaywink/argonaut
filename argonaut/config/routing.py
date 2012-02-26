"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False
    map.explicit = True

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE
    # main blog post url
    map.connect('blog_post', '/blog/{id}/{subject}', controller='blog', action='view', requirements={'id':'\d+'})
    # backup with slash
    map.connect('/blog/{id}/{subject}/', controller='blog', action='view', requirements={'id':'\d+'})
    # backup without subject
    map.connect('/blog/{id}/', controller='blog', action='view', requirements={'id':'\d+'})
    map.connect('/blog/{id}', controller='blog', action='view', requirements={'id':'\d+'})
    # fix for subjects with slashes
    map.connect('/blog/{id}/*subject', controller='blog', action='view', requirements={'id':'\d+'})
    # support for old basshero 2.0 urls
    map.connect('/{id}/{subject}', controller='blog', action='view', requirements={'id':'\d+'})
    map.connect('/{id}/{subject}/', controller='blog', action='view', requirements={'id':'\d+'})
    map.connect('/{id}/', controller='blog', action='view', requirements={'id':'\d+'})
    # generic blog url
    map.connect('/blog/{action}/{id}', controller='blog')
    # generic controller urls
    map.connect('/{controller}/{action}/{year}/{month}/{day}')
    map.connect('/{controller}/{action}/{id}')
    map.connect('/{controller}/{action}')
    # base mapped to first landing page
    map.connect('/', controller='landing', action='first_page')

    return map
