from argonaut.model.meta import Session, Base
from argonaut.model import Media

values = [
        [1,'42goals','/media/42goals.png'],
        [2,'Delicious','/media/delicious_32x32.png'],
        [3,'Diaspora*','/media/diaspora_32x32.png'],
        [4,'DZone','/media/DZone-32.png'],
        [5,'Email','/media/email-32.png'],
        [6,'Facebook','/media/FaceBook_32x32.png'],
        [7,'Geocaching.com','/media/Logo_Geocaching_32.png'],
        [8,'Google Reader','/media/Google-Reader-32.png'],
        [9,'Google Talk','/media/Google-Talk-32.png'],
        [10,'Youtube','/media/Google-YouTube-32.png'],
        [11,'Maemo.org','/media/maemo_org_32.png'],
        [12,'Picasa','/media/picasa_32.png'],
        [13,'Twitter','/media/Twitter_32x32.png']
        ]

def init_data():
    print "Initing media data"
    query = Session.query(Media)
    for rec in values:
        if not query.get(rec[0]):
            media = Media()
            media.id = rec[0]
            media.name = unicode(rec[1])
            media.url = unicode(rec[2])
            Session.add(media)
            Session.commit()





