import flask

app = flask.Flask(__name__)

@application.route('/')
def index(request):
    return '<h1>test</h1>'

if __name__ == '__main__':
    application.run()