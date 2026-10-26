
from random import randint

jogo = []
q = int(input('Quantos jogos você quer sortear?: '))
total = q

while q > 0:
    jogo = []

    for i in range(0, 7):
        n = randint(1, 60)

        while n in jogo:
            n = randint(1, 60)

        jogo.append(n)

    jogo.sort()
    print(f'{total - q + 1}° jogo: {jogo}')
    q -= 1
