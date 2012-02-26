import formencode

from pylons import tmpl_context as c, request

class CommentForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    body = formencode.validators.String(not_empty=True, max=4000)
    author = formencode.validators.String(not_empty=False, max=50)
    author_website = formencode.validators.URL(not_empty=False, add_http=True)
    post_id = formencode.validators.Number()
    antiSpam = formencode.validators.Number(not_empty=True, min=3, max=4)

class FilterForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    filter = formencode.validators.String(not_empty=True, max=50)
    
class PostForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    body = formencode.validators.String(not_empty=True)    
    subject = formencode.validators.String(not_empty=True, max=300)
    
def validate(schema):
    try:
        c.form_result = schema.to_python(dict(request.params))
        c.form_errors = {}
    except formencode.Invalid, error:
        c.form_result = error.value
        c.form_errors = error.error_dict or {}
        return False
    else:
        return True   

