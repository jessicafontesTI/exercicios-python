lista = []
c = 0

while True:
    dado = []

    nome = input("Digite seu nome: ")
    kg = float(input("Digite seu peso em kg: "))

    dado.append(nome)
    dado.append(kg)
    lista.append(dado)

    c += 1

    if c == 1:
        maior = menor = kg

    if kg > maior:
        maior = kg

    if kg < menor:
        menor = kg

    d = input("Deseja continuar? (S/N): ").strip().upper()[0]

    if d == 'N':
        break

print(f'\nVocê cadastrou {c} pessoas')

nomes_pesados = []
nomes_leves = []

for p in lista:
    if p[1] == maior:
        nomes_pesados.append(p[0])

    if p[1] == menor:
        nomes_leves.append(p[0])

print(f'As pessoas mais pesadas são: {", ".join(nomes_pesados)}, com {maior} kg')
print(f'As pessoas mais leves são: {", ".join(nomes_leves)}, com {menor} kg')

