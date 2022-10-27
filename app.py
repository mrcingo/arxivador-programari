import flask

from account import Account

app = flask.Flask(__name__)
accmanager = Account('sqlite3.db')

@app.route('/index')
def index():
    session = flask.request.cookies.get('SID')
    account_session = accmanager.session(session)
    print(account_session)
    if not account_session:
        return flask.render_template('index.html', cookie = 0)
    return flask.render_template('index.html', cookie = 1)

@app.route('/login')
def login():
    username = flask.request.args.get('username')
    password = flask.request.args.get('password')

    account = accmanager.login(username, password)

    if account:
        response = flask.make_response(
            flask.redirect('index.html')
        )
        response.set_cookie('SID', account['session'])

        return response
    return flask.render_template('register.html')

@app.route('/register')
def register():
    username = flask.request.args.get('username')
    password = flask.request.args.get('password')

    account = accmanager.register(username, password)
    if account:
        response = flask.make_response(
            flask.redirect('/index')
        )
        response.set_cookie('SID', account['session'])

        return response
    return flask.render_template('register.html')

if __name__ == "__main__":
    app.run()