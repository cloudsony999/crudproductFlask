import sqlite3 as s

def setDB():
    conn=s.connect('products.db')
    return conn
