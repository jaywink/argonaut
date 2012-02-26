from argonaut.model.meta import Session, Base
from argonaut.model import Page

values = [
        [1,'Blog',1,1,'/blog/latest',1],
        [2,'Archives',1,20,'/blog/archives',2],
        [3,'Tags',1,50,'/tag/show_all',3]
        ]

def init_data():
    print "Initing page data"
    query = Session.query(Page)
    for rec in values:
        if not query.get(rec[0]):
            page = Page()
            page.id = rec[0]
            page.name = unicode(rec[1])
            page.status = rec[2]
            page.page_order = rec[3]
            page.url = unicode(rec[4])
            page.type = rec[5]
            Session.add(page)
            Session.commit()





