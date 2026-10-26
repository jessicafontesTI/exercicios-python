from random import randint
from time import sleep

dicionario = {
    'Jogador_1': randint(1, 6),
    'Jogador_2': randint(1, 6),
    'Jogador_3': randint(1, 6),
    'Jogador_4': randint(1, 6)
}

for k, v in dicionario.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)

print('\n=== RANKING DOS JOGADORES ===')

ganhador = sorted(dicionario.items(), key=lambda item: item[1], reverse=True)

for pos, jogador in enumerate(ganhador, start=1):
    print(f'{pos}º lugar: {jogador[0]} com {jogador[1]}')
    sleep(1)