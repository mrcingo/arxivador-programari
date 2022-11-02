import sqlite3

import random
import string


class Account(sqlite3.Connection):

    def __init__(self, database: str = 'sqlite3.db') -> None:
        super().__init__(database=database)
        self.execute('''
CREATE TABLE IF NOT EXISTS accounts (
    id INT,
    username CHAR(255),
    password CHAR(255),
    sid CHAR(255)
)
                     ''')

    def account(self, username=None, sid=None):
        if not username and not sid:
            return {
                'message': 'No s\'ha donat cap paràmetre per iniciar la sessió.',
            }

        account = self.execute(
            f'SELECT * FROM accounts WHERE username = "{username}" OR sid = "{sid}";').fetchone()
        if account == None:
            return {
                'message': 'El compte amb el qual intenteu iniciar sessió ja no existeix.',
            }

        return {
            'message': 'La teva sessió o compte és existent.',
            'account': {
                'id': account[0],
                'username': username,
                'password': account[2],
                'sid': account[-1],
            }
        }

    def create(self, username, password) -> dict:
        if not username or not password:
            return {
                'message': 'No s\'ha donat un o cap paràmetre per crear la sessió.',
            }

        if self.account(username).get('account'):
            return {
                'message': 'El compte que intenteu crear ja està creat.',
            }

        id = self.execute(f'SELECT MAX(id) FROM accounts;').fetchone()[0]
        if not id:
            id = 0
        else:
            id += 1

        sid = ''.join(
            random.choices(
                string.ascii_letters + string.digits,
                k=32
            )
        )

        self.execute(
            f'INSERT INTO accounts VALUES ({id}, "{username}", "{password}", "{sid}");')
        self.commit()

        return {
            'message': 'El vostre compte està ara registrat a la base de dades.',
            'account': {
                'id': id,
                'username': username,
                'password': password,
                'sid': sid
            }
        }
