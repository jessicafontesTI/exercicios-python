lista = []
lista_par = []
lista_impar =[]

while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    d = input('Deseja continuar? (S/N): ').strip() .upper()[0]

    if d == 'N':
        break

    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

lista.sort()

print(f'A lista completa {lista}')
print(f"A lista dos números pares {lista_par}")
print(f'A lista dos números ímpares {lista_impar}')
