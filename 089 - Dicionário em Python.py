dicionario = {}

dicionario['nome'] = str(input("Digite o nome do Aluno: "))
dicionario['media'] = float(input("Digite a média do aluno: "))

print(f"O nome é igual {dicionario["nome"]}")
print(f"A média é igual a {dicionario["media"]}")

if dicionario['media'] >= 6:
    dicionario['situação'] = 'Aprovado'
    print(f"A Situação do aluno é: {dicionario['situação']}")
elif dicionario ['media'] < 3:
    dicionario['situação'] = 'Reprovado'
    print(f"A situação do aluno é: {dicionario['situação']}")
else:
    dicionario['situação'] = 'Recuperação'
    print(f"A situação do aluno é: {dicionario['situação']}")