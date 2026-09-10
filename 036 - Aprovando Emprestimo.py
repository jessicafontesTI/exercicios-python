casa = float(input('Digite o valor da casa que você quer comprar: '))
salario = float(input('Qual seu salário: '))
anos = int(input('Quantos anos de financiamento deseja: '))
prestacao = casa / (anos*12)

if prestacao >= (salario * 30/100):
    print(f'A prestação mensão ficou R${prestacao:.2f}\nE seu empréstimo foi NEGADO!')
else:
    print(f'A prestação mensal ficou R${prestacao:.2f}\n E seu empréstimo foi APROVADO!')