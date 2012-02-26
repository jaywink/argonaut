from argonaut.model.meta import Session, Base
from argonaut.model import Config

values = [
        ['rss_title','Argonaut RSS'],
        ['site_url','http://127.0.0.1:5000'],
        ['site_title','Argonaut'],
        ['comments_enabled','true']
        ]

def init_data():
    print "Initing config data"
    query = Session.query(Config)
    for rec in values:
        if not query.get(unicode(rec[0])):
            config = Config()
            config.id = unicode(rec[0])
            config.value = unicode(rec[1])
            Session.add(config)
            Session.commit()





