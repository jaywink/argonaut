from argonaut.model.meta import Session, Base
from argonaut.model import Social

values = [
        [1,'dummy.mail@example.com',1,50,'mailto:dummy.mail@example.com',5],
        [2,'Another social link',1,50,'http://www.example.com',10]
        ]

def init_data():
    print "Initing social data"
    query = Session.query(Social)
    for rec in values:
        if not query.get(rec[0]):
            social = Social()
            social.id = rec[0]
            social.name = unicode(rec[1])
            social.status = rec[2]
            social.priority = rec[3]
            social.url = unicode(rec[4])
            social.media_id = rec[5]
            Session.add(social)
            Session.commit()





