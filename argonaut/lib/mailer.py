from turbomail import Message

def send_mail(sender, to, subject, body):
    if sender and to and subject and body:
        message = Message(author=sender, to=to, subject=subject)
        message.rich = body
        # TODO: convert mail body to plain
        message.plain = 'This mail should be viewed in HTML.'
        try:
            message.send()
        except Exception, msg:
            if str(msg) == '[Errno 111] Connection refused':
                # caused by connection problem to smtp server
                pass
            else:
                # other error, raise
                raise Exception
            
