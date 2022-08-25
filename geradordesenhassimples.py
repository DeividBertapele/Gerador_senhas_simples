from multiprocessing.reduction import send_handle
from random import randint
loop = True

while loop:
    print('=========== GERENCIADOR DE SENHA ===========') # Gerenciadores de Senhas

    print('OPÇÕES: ') #opções
    print('[1] - Gerar uma nova senha.')
    print('[2] - Encerrar o programa.')
    senha = int(input('Escolha uma opção acima: '))

    if senha == 1:
        senha01 = int(input('Escolha um número qualquer: '))
        senha02 = int(input('Escolha outro um número final: '))
        for senha in range(0,8):
            novasenha = randint(senha01,senha02)
            print('Sua nova senha será: {}'.format(novasenha))
            1
    elif senha == 2:
        break

    else:
        print('Opção Inválida')