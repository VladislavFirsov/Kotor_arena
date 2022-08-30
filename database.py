import sqlite3


with sqlite3.connect('shop.db') as db:
    c = db.cursor()

    c.execute('''
              CREATE TABLE IF NOT EXISTS armor(
              id INTEGER PRIMARY KEY,    
              description TEXT                     
              name TEXT
              defence INTEGER
              dexterity bonus INTEGER
              strength bonus INTEGER
              wisdom bonus INTEGER
              
              
    ''')