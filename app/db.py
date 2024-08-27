import sqlite3

class DB:
    def __init__(self):
        self.con = sqlite3.connect('./dbsqlite.db')
        self.cur = self.con.cursor()

    def test(self):
        print('closed')
        self.con.close()
