from argonaut.model.meta import Session, Base
from argonaut.model import Boxes

values = [
        [1,1,1,1],
        [2,2,1,10],
        [3,3,1,30],
        [4,4,1,20]
        ]

def init_data():
    print "Initing boxes data"
    query = Session.query(Boxes)
    for rec in values:
        if not query.get(rec[0]):
            item = Boxes()
            item.box_id = rec[1]
            item.status = rec[2]
            item.order = rec[3]
            Session.add(item)
            Session.commit()





