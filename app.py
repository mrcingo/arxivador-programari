import flask

from account import Account

app = flask.Flask(__name__)
accmanager = Account('sqlite3.db')

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
    print(account)
    if account:
        response = flask.make_response(
            flask.redirect('index.html')
        )
        response.set_cookie('SID', account['session'])

        return response
    return flask.render_template('register.html')

if __name__ == "__main__":
    app.run()