import flask

application = flask.Flask(__name__)

@application.route('/')
def index(request):
    return '<h1>test</h1>'
