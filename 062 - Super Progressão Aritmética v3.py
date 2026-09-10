primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
contador = primeiro
i = 0
total = 0
termo = 10

while termo != 0:

    total = total + termo

    while i < total:

        print(contador, end=' ')

        if i < total - 1:
            print('>>', end=' ')
        else:
            print('!')

        contador = contador + razao
        i = i + 1

    termo = int(input("\nQuantos termos você quer mostrar mais? "))

print(f"Progressão foi finalizada com {total} termos mostrados")