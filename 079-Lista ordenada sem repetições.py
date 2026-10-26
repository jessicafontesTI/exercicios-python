
lista = []

valores = 0

for i in range(0, 5):
    valores = int(input("Digite um valor: "))
    print()

    if len(lista) == 0 or valores > lista[-1]:
        lista.append(valores)
        print('Adicionado ao final da lista\n')
        print()

    else:
        j = 0
        while j < len(lista):
            if valores <= lista[j]:
                lista.insert(j, valores)
                print(f"Adicionado na posição {j}")
                print()
                break
            j += 1

print(f'Os valores digitados foram {lista}')
   
