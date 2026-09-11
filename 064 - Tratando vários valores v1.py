numero = 0
contador = 0
soma = 0

while numero != 999:

    numero = int(input("Digite um número ou 999 para parar: "))

    if numero == 999:
        break

    contador = contador + 1
    soma =  soma + numero

print(f'Você digitou {contador} números e a soma deles é {soma}')
