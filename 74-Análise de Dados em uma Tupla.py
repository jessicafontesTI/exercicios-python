valores = []

for i in range(0, 4):
    valor = int(input("Digite um valor: "))
    valores.append(valor)

print(valores)

if 9 in valores:
    print(f'O valor 9 apareceu {valores.count(9)} veze(s)')
else:
    print('O valor 9 não apareceu')

if 3 in valores:
    print(f'O valor 3 aparece na posição {valores.index(3)}')
else:
    print('O valor 3 não foi digitado')

print('Valores pares:', end=' ')

for numero in valores:
    if numero % 2 == 0:
        print(numero, end=' ')
   
    