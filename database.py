import sqlite3

# conecta ao banco de dados (ou cria caso não haja um)
conn = sqlite3.connect('customer.db')

# cria um cursor
c = conn.cursor()

while True:
    first_name = input('First name: ')
    last_name = input('Last name: ')
    age = int(input('Age: '))
    option = input('Continue? (Y/N): ')

    c.execute('INSERT INTO customers VALUES (?, ?, ?)', (first_name, last_name, age))

    if option.upper() == 'N':
        break

# commita os comandos
conn.commit()

# fecha a conexão
conn.close()
