num = int(input('Digite um número para a tabuada: '))
cont = 0
for i in range (1 , 11):
    cont = cont + 1
    t = num * cont
    print(f'{cont} x {num} = {t}')
