import functions as f

f.create_table() # desativar após criar table

while True:
    print('\nadd - adicionar | rmv - remover | dat - ver dados | end - sair')
    f.line(64)
    option = input('comando: ').lower()

    match option:
        case 'add':
            fname = input('Primeiro nome: ')
            lname = input('Sobrenome: ')
            age = int(input('Idade: '))
            f.add_one(fname, lname, age)

        case 'rmv':
            id = input('ID: ')
            f.remove(id)

        case 'dat':
            f.show_all()

        case 'end':
            break
        case _:
            print('Comando inválido, tente novamente.')
