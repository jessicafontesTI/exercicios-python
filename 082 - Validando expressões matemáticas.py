e = str(input("Digite uma expressão:"))

abre = 0
fecha = 0

for c in e:
    if c == '(':
        abre += 1
    elif c == ')':
        fecha += 1

if abre == fecha:
    print('Sua expressão está correta!')
else: 
    print("Sua expressão está errada!")