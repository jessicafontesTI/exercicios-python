sexo = str(input('Digite seu sexo [M/F]: ')).strip() .upper()[0]
while sexo not in 'MmfF':
    sexo = str(input('Opção inválida, por favor informe seu sexo: ')).strip() .upper()[0]
    
print(f'{sexo}, sua resposta foi registrada')
