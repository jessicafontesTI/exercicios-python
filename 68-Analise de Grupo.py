print ('-=-='*10)
print ("----------CADASTRO DE PESSOAS-----------")
print ('-=-='*10)
c = 0
m = 0
f=0
while True:
    i = int(input("Idade: "))
    s = str(input('SEXO(M/F): ')).strip() .upper()[0]
    while not 'MF':
        s = input("Opção inválida! SEXO (M/F): ").strip().upper()[0]
    if i>18:
        c = c+1
    if s == 'M':
        m = m+1
    if s=='F' and i<20:
        f = f+1
    continuar = str(input("Quer continuar?(S/N): ")).strip() .upper()[0]
    while continuar not in "SN":
        continuar = input("Opção inválida! Quer continuar? (S/N): ").strip().upper()[0]
    if continuar == 'N':
        break

print(f"Total de pessoas com mais de 18 anos: {c}")
print(f"Ao todo temos {m} homen(s) cadastrados")
print(f'E temos {f} mulher com menos de 20 anos')