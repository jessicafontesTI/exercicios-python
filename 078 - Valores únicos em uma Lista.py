
lista = []

continua = 'S'

while continua == 'S':

    valores = int(input("Digite um valor: "))

    if valores in lista:
        print('Esse número já existe, não irei adicioná-lo')
    else:
        lista.append(valores)

    continua = input('Deseja continuar (S/N)? ').strip().upper()

    lista.sort

print(f'Os valores digitados foram: {lista}')
