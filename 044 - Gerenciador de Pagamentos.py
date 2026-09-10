print('----' * 22)
print  ('----' * 9,'LOJAS FONTES','----' * 9,'--')
print('----' * 22) 

valor = float(input('Qual o valor a ser pago? R$: '))
condicao = int(input(' [1]-Á vista ou cheque\n [2]-Á vista no cartão\n [3]-Duas vezes no cartão\n [4]-Três ou mais\n Escolha uma opção: '))

if condicao == 1:
    a1 = valor - (valor * 10/100)
    print(f'Seu total com desconto de 10% é R${a1}')
elif condicao == 2:
    a2 = valor - (valor * 5/100)
    print(f'Seu total com desconto de 5% é R${a2}')
elif condicao == 3:
    a3 = valor / 2
    print(f'Dividindo o valor em duas vezes, cada parcela ficou R${a3}')
elif condicao == 4:
    a4 = valor + (valor * 20/100)
    parcela = int(input('Quantas vezes você quer parcelar? '))
    total = a4 / parcela
    print(f'Sua compra parcelada em {parcela}x de {total:.2f} com JUROS')
    print(f'Sua compra de {valor} vai custar R${a4} no final')

