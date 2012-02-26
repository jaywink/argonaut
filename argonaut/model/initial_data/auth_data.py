from argonaut.model.meta import Session, Base
from argonaut.model.auth import User, Group, Permission, User_Group, Group_Permission

user_values = [
        [1,'admin','admin@change.this.to.a.real.domain','admin','Administrator']
        ]
        
group_values = [
        [1,'Administrator'],
        [2,'Editor']
    ]
    
permission_values = [
        [1,'Write post'],
        [2,'Edit post']
    ]
    
user_group_values = [
        [1,1,1]
    ]
    
group_permission_values = [
        [1,1,1],
        [2,1,2],
        [3,2,1],
        [4,2,2]
    ]   

def init_data():
    print "Initing auth data"
    query = Session.query(User)
    for rec in user_values:
        if not query.get(unicode(rec[0])):
            user = User()
            user.username = unicode(rec[1])
            user.email = unicode(rec[2])
            user._set_password(unicode(rec[3]))
            user.name = unicode(rec[4])
            Session.add(user)
            Session.commit()
            
    query = Session.query(Group)
    for rec in group_values:
        if not query.get(unicode(rec[0])):
            group = Group()
            group.name = unicode(rec[1])
            Session.add(group)
            Session.commit()
            
    query = Session.query(Permission)
    for rec in permission_values:
        if not query.get(unicode(rec[0])):
            permission = Permission()
            permission.name = unicode(rec[1])
            Session.add(permission)
            Session.commit()

    query = Session.query(User_Group)
    for rec in user_group_values:
        if not query.get(unicode(rec[0])):
            user_group = User_Group()
            user_group.user_id = unicode(rec[1])
            user_group.group_id = unicode(rec[2])
            Session.add(user_group)
            Session.commit()

    query = Session.query(Group_Permission)
    for rec in group_permission_values:
        if not query.get(unicode(rec[0])):
            group_permission = Group_Permission()
            group_permission.group_id = unicode(rec[1])
            group_permission.permission_id = unicode(rec[2])
            Session.add(group_permission)
            Session.commit()
