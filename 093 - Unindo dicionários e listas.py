cadastro = {}
lista = []
media = cn = 0
mulheres = []

while True:
    cadastro['nome'] = str(input("Nome: "))

    cadastro['sexo'] = str(input("Digite o sexo (M/F): ")).upper().strip()[0]
    while cadastro['sexo'] not in 'MF':
        print('ERRO! Digite somente M ou F')
        cadastro['sexo'] = str(input("Digite o sexo (M/F): ")).upper().strip()[0]

    if cadastro['sexo'] == 'F':
        mulheres.append(cadastro['nome'])

    cadastro['idade'] = int(input("Idade: "))

    cn += 1
    media += cadastro['idade']

    lista.append(cadastro.copy())
    cadastro.clear()

    continuar = str(input("Quer continuar? (S/N): ")).upper().strip()[0]
    while continuar not in 'SN':
        print('ERRO! Digite somente S ou N')
        continuar = str(input("Quer continuar? (S/N): ")).upper().strip()[0]

    if continuar == 'N':
        break

r = media / cn

print(f'A) Ao todo temos {cn} pessoas cadastradas')
print(f'B) A média de idade é de {r}')
print(f'C) As mulheres cadastradas foram {mulheres}')
print('D) Lista das pessoas com idade acima da média:')
for pessoa in lista:
    if pessoa['idade'] > r:
        print(f"Nome: {pessoa['nome']}; Sexo: {pessoa['sexo']}; Idade: {pessoa['idade']}")
