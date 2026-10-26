cadastro = {}
c = gol = 0
lista = []
cadastro['nome'] = str(input("Digite o nome do jogador: "))
partida = int(input(f"Quantas partidas {cadastro['nome']} jogou ? "))

for i in range(partida):
    gol = int(input(f'Quantos gols na partida {i+1}? '))
    lista.append(gol)
    c =  c + gol

cadastro['gols'] = lista
cadastro['total'] = c

print(cadastro)

print('==' * 30)
for k, v in cadastro.items():
    print(f'o Campo {k} tem valor {v}')

print('==' * 30)
print(f'O {cadastro["nome"]} jogou {partida} partidas')
for i in range(partida):
    print(f'Na partida {i+1} ele fez {gol} gols')
print(f'Foi um total de {cadastro['total']} gols')