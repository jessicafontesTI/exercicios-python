import random
import time

tentativa = 0
pc = random.randint(0, 10)
print('Sou o computador\nEstou pensando em um número de 0 a 10\n')

jogando = True

while jogando:
    numero = int(input("Digite aqui seu palpite do que estou pensando: "))
    tentativa = tentativa + 1
    if numero == pc:
        print(f'Parabéns, você acertou, pensei no número {pc} e você acertou com {tentativa} tentativas!')
        break
    if numero < pc:
        print('Mais...Tente novamente')
    elif numero > pc:
        print('Menos...Tente novamente')
