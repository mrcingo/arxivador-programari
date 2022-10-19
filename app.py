import flask
from manage import Manage


app = flask.Flask(__name__)
manager = Manage('sqlite3.db')

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/login', methods = ['GET'])
def login():
    username = flask.request.args.get('username')
    password = flask.request.args.get('password')
    client = manager.exist(username, password)
    return flask.jsonify(client)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    username = flask.request.args.get('username')
    password = flask.request.args.get('password')
    if username and password:
        client = manager.create(username, password)
        print(client)
        if client:
            return flask.jsonify(client)
    return flask.render_template('register.html')

if __name__ == "__main__":
    app.run()