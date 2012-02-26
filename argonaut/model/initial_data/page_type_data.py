from argonaut.model.meta import Session, Base
from argonaut.model import Page_Type

values = [
        [1,'blog','blog','latest',''],
        [2,'archives','blog','archives',''],
        [3,'tags','tag','show_all',''],
        [4,'custom','page','show',''],
        [5,'pwi_gallery','page','show','pwi_gallery']
        ]

def init_data():
    print "Initing page_type data"
    query = Session.query(Page_Type)
    for rec in values:
        if not query.get(rec[0]):
            page_type = Page_Type()
            page_type.id = rec[0]
            page_type.name = unicode(rec[1])
            page_type.controller = unicode(rec[2])
            page_type.action = unicode(rec[3])
            page_type.param = unicode(rec[4])
            Session.add(page_type)
            Session.commit()





