import flask
import json

app = flask.Flask(__name__)
                     
# modelos de prueba

@app.route('/test/index')
def test_index():
    return flask.render_template('tests/index.html')

@app.route('/test/login')
def test_login():
    with open('users.json', 'r') as fr:
        users: dict = json.load(fr)
    if users.get(flask.request.args.get('username')):
        return flask.redirect('/test/index')
    return flask.render_template('tests/login.html')

@app.route('/test/register')
def test_register():
    with open('users.json', 'r') as fr:
        users: dict = json.load(fr)
    print(users)
    users[flask.request.args.get('username')] = users[flask.request.args.get('password')]

    if not users.get(flask.request.args.get('username')) and flask.request.args.get('username') and flask.request.args.get('password'):
        with open('users.json', 'w') as fw:
            print(users) 
            json.dump(users, fw)
        return flask.redirect('/test/index')
    return flask.render_template('tests/register.html')

# modelos de produccion

@app.route('/index')
def index():
    return flask.render_template('production/index.html')

@app.route('/login')
def login():
    return flask.render_template('production/login.html')

@app.route('/register')
def register():
    return flask.render_template('production/register.html')

if __name__ == '__main__':
    app.run()