from argonaut.model.meta import Session, Base
from argonaut.model import Box

values = [
        [1,'Tag cloud','/boxes/tag_cloud.mako'],
        [2,'Search','/boxes/search.mako'],
        [3,'Account','/boxes/account.mako'],
        [4,'Social','/boxes/social.mako']
        ]

def init_data():
    print "Initing box data"
    query = Session.query(Box)
    for rec in values:
        if not query.get(rec[0]):
            item = Box()
            item.name = unicode(rec[1])
            item.template = unicode(rec[2])
            Session.add(item)
            Session.commit()





