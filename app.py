import flask
from manage import Manage


app = flask.Flask(__name__)
manager = Manage('sqlite3.db')

@app.route('/')
def index():
    print(manager.session(flask.request.cookies.get('SID')))
    if manager.session(flask.request.cookies.get('SID')):
        if flask.request.args.get('username'):
            print('a')
            return flask.redirect(f'/register?username={flask.request.args.get("username")}')
        return flask.render_template('index.html')
    else:
        return flask.redirect('/login')

@app.route('/logout')
def logout():
    if flask.request.cookies.get('SID'):
        flask.request.cookies.pop('SID')
        return flask.redirect('/login')
    return '<h1>Not loged in.</h1>'

@app.route('/login', methods = ['GET'])
def login():
    username = flask.request.args.get('username')
    password = flask.request.args.get('password')
    
    client = manager.exist(username, password)
    if client:
        response = flask.make_response(flask.redirect('/'))
        response.set_cookie('SID', client[-1])
        return response
    return flask.render_template('login.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    username = flask.request.args.get('username')
    password = flask.request.args.get('password')

    client = manager.create(username, password)
    if client:
        response = flask.make_response(flask.redirect('/'))
        response.set_cookie('SID', client['sid'])
        return response
    return flask.render_template('register.html')

if __name__ == "__main__":
    app.run()