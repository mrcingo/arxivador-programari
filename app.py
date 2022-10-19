import flask
from manage import Manage


app = flask.Flask(__name__)
manager = Manage('sqlite3.db')

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/login')
def login():
    return manager.exist(flask.request.args.get('username'), flask.request.args.get(
        'password')) if flask.request.args.get('username') and flask.request.args.get(
        'password') else None
    return flask.render_template('login.html')

@app.route('/register', METHODS = ['GET', 'POST'])
def register():
    username = flask.request.args.get('username')
    password = flask.request.args.get('password')
    if username and password:
        client = manager.create(username, password)
        if client:
            return flask.jsonify(client)
    return flask.render_template('register.html')

if __name__ == "__main__":
    app.run()