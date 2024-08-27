import sqlite3

class DB:
    def __init__(self):
        self.con = sqlite3.connect('./db.sqlite')
        self.cur = self.con.cursor()

    def test(self):
        print('closed')
        self.con.close()
