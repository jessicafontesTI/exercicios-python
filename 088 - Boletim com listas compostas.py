
lista = []

while True:
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    lista.append([nome, nota1, nota2, media])

    d = input("Quer continuar? (S/N): ").strip().upper()[0]

    if d == 'N':
        break


print(f'{"Nº":<4}{"NOME:":<10}{"MÉDIA:":<8}')

for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[3]:<8.1f}')


while True:
    consulta = int(input(
        "Gostaria de ver as notas de quem? "
        "Digite o número do aluno (ou 999 para sair): "
    ))

    if consulta == 999:
        break

    if consulta >= 0 and consulta < len(lista):
        aluno = lista[consulta]

        print(f"Aluno: {aluno[0]}")
        print(f"Primeira nota: {aluno[1]}")
        print(f"Segunda nota: {aluno[2]}")
        print(f"Média: {aluno[3]:.1f}")
    else:
        print("Número de aluno inválido!")
