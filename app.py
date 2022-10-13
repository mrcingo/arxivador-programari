import flask

app = flask.Flask(__name__)
                     
# modelos de prueba

@app.route('/test/index')
def test_index():
    return flask.render_template('tests/index.html')

@app.route('/test/login')
def test_login():
    return flask.render_template('tests/login.html')

@app.route('/test/register')
def test_register():
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