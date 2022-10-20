from sqlite3 import Connection
from random import choices
from string import ascii_letters, digits


class Manage(Connection):

    def __init__(self, database: str) -> None:
        super().__init__(database)
        self.execute('CREATE TABLE IF NOT EXISTS clients (id INT, username CHAR(255), password CHAR(255), session CHAR(255));')

    def create(self, username: str, password: str) -> dict[str, str] | None:
        if self.execute(f'SELECT * FROM clients WHERE username=\'{username}\'').fetchone() is None:
            id = self.execute(f'SELECT MAX(id) FROM clients').fetchone()
            sid = "".join(choices(digits + ascii_letters, k = 32))            

            self.execute(f'INSERT INTO clients (id, username, password, session) VALUES ({id[0] + 1 if id[0] != None else 0}, \"{username}\", \"{password}\", \"{sid}\")')
            self.commit()
            return {'username': username, 'password': password, 'sid': sid}
        return

    def session(self, sid: str) -> bool:
        print(sid)
        print(self.execute(f'SELECT * FROM clients WHERE session=\"{sid}\";').fetchone())
        return True if self.execute(
            f'SELECT * FROM clients WHERE session=\"{sid}\"').fetchone() != None else False

    def exist(self, username: str, password: str) -> dict | None:
        client = self.execute(f'SELECT * FROM clients WHERE username=\'{username}\'').fetchone()
        if client is not None:
            return client
        return 