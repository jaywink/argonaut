<%
    try:
        if c.login_counter:
            pass
    except:
        try:
            c.login_counter = request.environ['repoze.who.logins'] + 1
        except:
            c.login_counter = 1
    try:
        if c.came_from:
            pass
    except:
        c.came_from = '/'
    if c.login_counter > 1:
        context.write('Incorrect username or password')
%>
<div class="no_overflow">
<form action="${h.url(controller='account', action='login_handler'
,came_from=c.came_from, __logins=c.login_counter)}" method="POST">
<table id="login">
    <tr>
        <td><label for="login">Username:</label></td>
        <td>${h.text('login', size=20)}</td>
    </tr>
    <tr>
        <td><label for="password">Password:</label></td>
        <td>${h.password('password', size=20)}</td>
    </tr>
</table>
${h.submit('submit', 'Submit')}
</form>
</div>
