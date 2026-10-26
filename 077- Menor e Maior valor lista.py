valores = []

for i in range(0, 5):
    valor = int(input(f'Digite um valor para a posição {i}: '))
    valores.append(valor)

maior = max(valores)
menor = min(valores)

para_maior = []

for j in range(0, 5):
    if valores[j] == maior:
        para_maior.append(j)

para_menor = []

for j in range(0, 5):
    if valores[j] == menor:
        para_menor.append(j)

print(f'O maior valor é {maior} e está na(s) posiçõe(s) {para_maior}')
print(f'O menor valor é {menor} e está na(s) posiçõe(s) {para_menor}')