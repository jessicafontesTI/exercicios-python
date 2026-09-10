from random import randint
import time
print('------' *5, 'JOGO','------'*5)
itens = int(input(' Vamos jogar?\n [1]-Papel\n [2]-Pedra\n [3]-Tesoura\nEscolha sua opção: '))

print('\033[1;31mJO\nKEN\nPO\033[m')
print('\033[32mPROCESSANDO\033[m')
time.sleep(3)
print('=-=-=' * 5)

if itens == 1:
    print(f'Você escolheu Papel')
elif itens == 2:
    print(f'Você escolheu Pedra')
elif itens == 3:
    print(f'Você escolheu Tesoura')

computador = randint(1, 3)

if computador == 1:
    print(f'O computador escolheu Papel')
elif computador == 2:
    print(f'O computador escolheu Pedra')
elif computador == 3:
    print(f'O computador escolheu Tesoura')

print('=-=-=' * 5)

if itens == 1 and computador == 1:
    print('JOGUE DE NOVO')
elif itens == 2 and computador == 2:
    print('JOGUE DE NOVO')
elif itens == 3 and computador == 3:
    print('JOGUE DE NOVO')

elif itens == 1 and computador == 2:
    print('VOCÊ GANHOU')

elif itens == 2 and computador == 1:
    print('COMPUTADOR GANHOU')

elif itens == 2 and computador == 3:
    print('VOCÊ GANHOU')

elif itens == 3 and computador == 2:
    print('COMPUTADOR GANHOU')

elif itens == 1 and computador == 3:
    print('COMPUTADOR GANHOU')

elif itens == 3 and computador == 1:
    print('VOCÊ GANHOU')
