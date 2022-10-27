import flask

from account import Account

app = flask.Flask(__name__)
accmanager = Account('sqlite3.db')

@app.route('/login')
def login():
    username = flask.request.form.get('username')
    password = flask.request.form.get('password')

    return flask.jsonify(accmanager.login(username, password))
    

if __name__ == "__main__":
    app.run()