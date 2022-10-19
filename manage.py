import sqlite3


class Manage(sqlite3.Connection):

    def __init__(self, database: str) -> None:
        super().__init__(database)
        self.execute('CREATE TABLE IF NOT EXISTS clients (id INT, username CHAR(255), password CHAR(255));')

    def create(self, username: str, password: str) -> dict[str, str]:
        if self.execute(f'SELECT * FROM clients WHERE username=\'{username}\'').fetchone() is None:
            id = self.execute(f'SELECT MAX(id) FROM clients').fetchone()
            self.execute(f'INSERT INTO clients (id, username, password) VALUES ({id[0] + 1 if id[0] != None else 0}, \"{username}\", \"{password}\")')
            self.commit()
            return {'username': username, 'password': password}
        return

    def exist(self, username: str, password: str) -> bool:
        client = self.execute(f'SELECT * FROM clients WHERE username=\'{username}\'').fetchone()
        if client is not None:
            return client
        return 