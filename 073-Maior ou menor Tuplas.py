from random import randint

a = randint(1,10)
b = randint(1,10)
c = randint(1,10)
d = randint(1,10) 
e = randint(1,10) 


numeros = (a, b, c, d, e)
print(f'{numeros}')
s = sorted(numeros)
print(f'O menor número da Tupla é {s[0]}')
print(f'O menor número da Tupla é {s[4]}')
