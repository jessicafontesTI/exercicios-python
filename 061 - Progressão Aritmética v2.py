primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

contador = primeiro
i = 0

while i < 10:

    print(contador, end=' ')

    if i < 9:
        print('>>', end=' ')
    else:
        print('!')

    contador = contador + razao
    i = i + 1