import sqlite3


class DbAccess:


    def insert_number(self, name, number):
        con = sqlite3.connect('te.db')
        cur = con.cursor()
        cur.execute("INSERT INTO phone_numbers (name,phone_numbers) VALUES (? ,?)", ("Michael", "0876665555"))
        con.commit()
        con.close()
