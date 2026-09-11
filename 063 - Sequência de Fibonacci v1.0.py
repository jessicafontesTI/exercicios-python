n1 = 0
n2 = 1
n3 = 0
contador = 3

termo = int(input('Quantos termos você quer mostrar?: '))

print(f'{n1} >> {n2}', end=" ")

while contador <= termo:

    n3 = n1 + n2

    print(f'>> {n3}', end=" ")

    n1 = n2
    n2 = n3

    contador = contador + 1
