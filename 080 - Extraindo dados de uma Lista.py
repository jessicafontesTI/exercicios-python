lista = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)

    d = input('Deseja continuar? (S/N): ').strip().upper()[0]

    if d == 'N':
        break

if 5 in lista:
    print('Existe o número 5 na lista!')
else:
    print('Não existe o número 5 na lista!')
lista.sort(reverse=True)
c = len(lista)


print(f'A lista completa {lista}')
print(f"Você digitou {c} valores")