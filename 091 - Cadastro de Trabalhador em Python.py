from datetime import datetime
cadastro = {}

cadastro['Nome'] = str(input("Nome: "))
nascimento = int(input('Ano de nascimento: '))
cadastro['Idade'] = datetime.now().year - nascimento
cadastro['Carteira'] = int(input("Carteira de trabalho (0 não tem): "))

if cadastro['Carteira'] != 0:
    cadastro['Ano'] = int(input("Ano de contratação: "))
    cadastro['Salário'] = float(input("Salário:R$ "))
    cadastro['Aprosentadoria'] = cadastro['Idade'] + (cadastro['Ano'] + 35) - datetime.now().year

print('==_==' * 10) 
for k, v in cadastro.items():
    print(f"{k} tem valor {v}")