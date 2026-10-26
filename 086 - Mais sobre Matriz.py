
matriz = [[], [], []]
par = soma = 0

for i in range(0, 3):
    n = int(input('Digite um valor: '))
    matriz[0].append(n)

for i in range(0, 3):
    n = int(input('Digite um valor: '))
    matriz[1].append(n)

for i in range(0, 3):
    n = int(input('Digite um valor: '))
    matriz[2].append(n)

for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end='')

        if valor % 2 == 0:
            par += valor

    print()

soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
maior = max(matriz[1])

print(f'A soma de todos os números pares é: {par}')
print(f'A soma da terceira coluna é: {soma}')
print(f'O maior número da segunda linha é: {maior}')
