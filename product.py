import sqlite3
import account


class Product(sqlite3.Connection):

    def __init__(self, session,) -> None:
        self.session = session
        self.account = account.Account('sqlite3.db').account(sid=session)
        print(self.account)

        super().__init__('sqlite3.db')

        self.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INT,
    account CHAR(255),
    name CHAR(255),
    amount INT
)
                     ''')

    def products(self):
        if not self.account.get('account'):
            return {
                'message': 'La compte que s\'ha donat no existeix en la base de dades.',
            }

        request = self.execute(
            f'SELECT * FROM products WHERE account = "{self.session}";').fetchall()

        if not request:
            return {
                'message': 'La conta no te productes en la base de dades.'
            }

        products = []
        for _ in range(len(request)):
            for i in range(len(request)):
                try:
                    if request[i + 1][0] > request[i][0]:
                        previous = request[i]
                        request[i] = request[i + 1]
                        request[i + 1] = previous
                except IndexError:
                    pass

        products = []
        for product in request:
            products.append(
                {
                    'id': product[0],
                    'account': product[1],
                    'name': product[2],
                    'amount': product[-1]
                }
            )

        return {
            'message': 'Compte trobat, aquí tens tots els seus productes.',
            'products': products
        }

    def create(self, name, amount) -> dict:
        if not self.account.get('account'):
            return {
                'message': 'La compte que s\'ha donat no existeix en la base de dades.',
            }

        if self.product(name).get('product'):
            return {
                'message': 'Producte ja creat.'
            }

        id = self.execute(
            f'SELECT * FROM products WHERE account = "{self.session}"').fetchall()
        self.execute(
            f'INSERT INTO products VALUES ({len(id) + 1 if id else 0}, "{self.session}", "{name}", {amount})')
        self.commit()

        return {
            'message': 'Producte afegit a la base de dades.',
            'product': {
                'account': self.session,
                'id': id,
                'name': name,
                'amount': amount,
            }
        }

    def product(self, name=None, id=None):
        
        if name:
            product = self.execute(
                f'SELECT * FROM products WHERE account = "{self.session}" AND name = "{name}";').fetchone()

        elif id != None:
            product = self.execute(
                f'SELECT * FROM products WHERE account = "{self.session}" AND id = {id};').fetchone()

        elif not id and not name:
            return {
                'message': 'No s\'ha donat cap paràmetre.'
            }

        if not product:
            return {
                'message': 'No s\'ha trobat el producte a la base de dades.'
            }

        return {
            'message': 'Producte trobat, aquí tens el resultat.',
            'product': {
                'id': product[0],
                'account': self.session,
                'name': product[2],
                'amount': product[-1]
            }
        }

    def delete(self, id):
        if not self.account.get('account'):
            return {
                'message': 'La compte que s\'ha donat no existeix en la base de dades.',
            }

        if not self.product(id=id).get('product'):
            return {
                'message': 'El producte actual que has donat no es troba a la base de dades.'
            }

        self.execute(
            f'DELETE FROM products WHERE account = "{self.session}" AND id = {id};')
        self.commit()

        return {
            'message': 'Producte eliminat.'
        }
