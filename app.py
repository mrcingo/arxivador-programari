import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return '<h1>test</h1>'

if __name__ == '__main__':
    app.run()