import sqlite3

def line(length):
    print('-'*length)

def create_table():
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE people 
    (first_name TEXT, 
    last_name TEXT, 
    age INTEGER)''')

def add_one(fname, lname, age):
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()

    c.execute('INSERT INTO people VALUES (?,?,?)', (fname, lname, age))

    conn.commit()
    conn.close()

def remove(id):
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()

    c.execute('DELETE from people WHERE rowid = ?', id)

    conn.commit()
    conn.close()

def show_all():
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()

    c.execute('SELECT rowid, * FROM people')

    items = c.fetchall()
    print('\nID    | Nome          | Sobrenome     | Idade')
    line(42)
    for item in items:
        #print(f'{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}'.expandtabs(16))
        print(f'{item[0]}\t', end='')
        print(f'{item[1]}\t'.expandtabs(16), end='')
        print(f'{item[2]}\t'.expandtabs(16), end='')
        print(f'{item[3]}\t', end='\n')
    
    conn.close()
