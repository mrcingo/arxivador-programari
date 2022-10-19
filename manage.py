import sqlite3


class Manage(sqlite3.Connection):

    def __init__(self, database: str) -> None:
        super().__init__(database)
        self.execute('''
        CREATE TABLE clients 
        IF NOT EXISTS 
        (id INT, username CHAR(255), password CHAR(255));
        ''')

    def create(self, username: str, password: str) -> dict[str, str]:
        password = password.encode()
        if self.execute(f'SELECT * FROM clients WHERE username=\'{username}\'').fetchone() is None:
            id = self.execute(f'SELECT MAX(id) FROM clients').fetchone()
            self.execute(f'INSERT INTO clients (id, username, password) VALUES ({id + 1 if id != None else 0}, \"{username}\", \"{password}\")')
            return {'username': username, 'password': password}
        return