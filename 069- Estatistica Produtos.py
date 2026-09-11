print('-=-=' * 10)
print("             LOJA BARATÃO")
print('-=-=' * 10)

soma = 0
mil = 0
menor = 0
nome_menor = " "

while True:

    nome = input("Digite o nome do produto: ")

    produto = float(input("Digite o valor do produto: R$ "))

    soma = soma + produto

    if produto > 1000:
        mil = mil + 1

    if menor == 0 or produto < menor:
        menor = produto
        nome_menor = nome

    decisao = input("Deseja continuar? [S/N]: ").strip().upper()[0]

    while decisao not in "SN":
        decisao = input("Opção inválida! Deseja continuar? [S/N]: ").strip().upper()[0]

    if decisao == "N":
        break
print('-=-='*10)
print('           FIM DO PROGRAMA')
print('-=-='*10)
print(f"O total da compra foi R$ {soma:.2f}")
print(f"Temos {mil} produto(s) que custam mais de R$ 1000")
print(f"O produto mais barato foi {nome_menor}, que custou R$ {menor:.2f}")
