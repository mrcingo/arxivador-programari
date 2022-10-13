import flask

app = flask.Flask(__name__)

@app.route('/test/index')
def index():
    return flask.render_template('tests/index.html')

@app.route('/test/login')
def index():
    return flask.render_template('tests/login.html')

@app.route('/test/register')
def index():
    return flask.render_template('tests/register.html')

if __name__ == '__main__':
    app.run()