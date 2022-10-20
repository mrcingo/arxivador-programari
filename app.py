import flask
from manage import Manage


app = flask.Flask(__name__)
manager = Manage('sqlite3.db')

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/logout')
def logout():
    if flask.request.cookies.get('SID'):
        response = flask.make_response(flask.redirect('/login'))
        response.set_cookie('SID', '', expires=0)
        return response
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
    return flask.render_template('register.html', name = "test")

if __name__ == "__main__":
    app.run()