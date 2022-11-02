import flask

from account import Account
from product import Product

empresa = flask.Flask(__name__)


@empresa.route('/')
def index():
    if Account().account(sid=flask.request.cookies.get('SID')).get('account'):
        return flask.render_template('index.html', session=True)
    return flask.render_template('index.html', session=False)


@empresa.route('/login')
def login():
    message = ''

    account = Account().account(
        flask.request.args.get('username')
    )
    message = account['message']

    try:
        if account.get('account').get('password') != flask.request.args.get('password'):
            message = 'La contrasenya donada no és correcta!'

        elif message == 'La teva sessió o compte és existent.':
            message = 'Has iniciat sessió.'

            response = flask.make_response(
                flask.render_template('login.html', message=message))
            response.set_cookie('SID', account.get('account')['sid'])

            return response
    except AttributeError:
        pass

    return flask.render_template('login.html', message=message)


@empresa.route('/register')
def register():
    message = ''

    account = Account().create(
        flask.request.args.get('username'),
        flask.request.args.get('password')
    )
    message = account['message']

    try:

        if account.get('account'):
            message = 'Has iniciat sessió.'

            response = flask.make_response(
                flask.render_template('register.html', message=message))
            response.set_cookie('SID', account.get('account')['sid'])

            return response
    except AttributeError:
        pass

    return flask.render_template('register.html', message=message)


@empresa.route('/logout')
def logout():
    response = flask.make_response(flask.redirect('/login'))
    if flask.request.cookies.get('SID'):
        response.set_cookie('SID', '', expires=0)
    return response

@empresa.route('/products')
def products():
    account_products_manager = Product(flask.request.cookies.get('SID'))
    return flask.render_template('products.html', account=account_products_manager.products())

@empresa.route('/products/delete')
def delete():
    if not flask.request.args.get('id'):
        return flask.redirect('/products')

    account_products_manager = Product(flask.request.cookies.get('SID'))
    account_products_manager.delete(int(flask.request.args.get('id')))

    return flask.redirect('/products')

@empresa.route('/products/create')
def create():
    if not flask.request.args.get('name') and not flask.request.args.get('amount'):
        return flask.redirect('/products')

    account_products_manager = Product(flask.request.cookies.get('SID'))
    product = account_products_manager.create(flask.request.args.get('name'), int(flask.request.args.get('amount')))

    if not product.get('product'):
        return f'''
<h1>Alguna cosa està malament!</h1>
<p>{product.get('message')}</p>
        '''

    return flask.redirect('/products')


if __name__ == '__main__':
    empresa.run(debug=False)
