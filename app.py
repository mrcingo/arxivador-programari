import flask
import json

app = flask.Flask(__name__)


@app.route('/')
def index():
    with open('users.json', 'w') as file:
        if not flask.request.cookies('SID'):
            return '<h1>No has creat una sesio!</h1>\n<h3>Aixi que no pots acceir al producte<h3>'
    return flask.render_template('tests/index.html')

@app.route('/login')
def login():
    if flask.request.cookies.get('SID'):
        return '<h1>Ja estas registrat!</h1>'
    if not flask.request.args.get('username'
    ) and flask.request.args.get('password'):
        return flask.render_template('tests/login.html')

    with open('users.json', 'r') as file:
        if json.load(file).get(flask.request.args.get('username')
        ) == flask.request.args.get('password'):
            response = flask.make_response(flask.redirect('/index'))
            response.set_cookie('SID', '1')
            return response
        else:
            return flask.render_template('tests/login.html')

@app.route('/register')
def register():
    if flask.request.cookies.get('SID'):
        return '<h1>Ja estas registrat!</h1>'
    if not flask.request.args.get('username'
    ) and flask.request.args.get('password'):
        return flask.render_template('tests/register.html')

    with open('users.json', 'r') as file:
        if not json.load(file).get(flask.request.args.get('username')):
            response = flask.make_response(flask.redirect('/index'))
            response.set_cookie('SID', '1')
            users = json.load(file)
            users[flask.request.args.get('username')] = flask.request.args.get('password')
            json.dump(file, users)
            return response
        else:
            return flask.render_template('tests/login.html')