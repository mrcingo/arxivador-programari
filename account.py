from sqlite3 import Connection

from string import ascii_letters, digits
from random import choices


class Account(Connection):

    def __init__(self, database: str) -> None:
        super().__init__(database)
        self.execute(
            '''
            CREATE TABLE IF NOT EXISTS accounts 
            (
                id INT, 
                username CHAR(255), 
                password CHAR(255), 
                session CHAR(255)
            );
            ''')

    def register(self, username: str, password: str) -> dict | None:
        account = self.execute(f'SELECT * FROM accounts WHERE username="{username}"').fetchone()

        if not username or not password:
            return None

        if account:
            return None

        identificator = self.execute(f'SELECT MAX(id) FROM accounts').fetchone()
        print(identificator)
        if not identificator[0]: identificator = 0
        else: identificator = identificator[0] + 1

        session = choices(
            ascii_letters + digits,
            k = 32
        )

        self.execute(f'''
        INSERT INTO accounts 
        (id, username, password, session) VALUES 
        ({identificator}, "{username}", "{password}", "{session}")
        ''')
        self.commit()

        return {
            'id': identificator, 
            'username': username, 
            'password': password,
            'session': session
        }

    def login(self, username: str, password: str):
        account = self.execute(f'SELECT * FROM accounts WHERE username="{username}"').fetchone()
        
        if not account:
            return None

        return {
            'id': account[0],
            'username': account[1],
            'password': account[2],
            'session': account[3]
        }