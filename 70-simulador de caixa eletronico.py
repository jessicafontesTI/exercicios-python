print('>..>..' * 10)
print('                   BANCO DA JÉSSICA')
print('>..>..' * 10)

valor = int(input("Qual valor você deseja sacar? R$ "))

cinquenta = 0
vinte = 0
cinco = 0
real = 0

while valor >= 50:
    valor = valor - 50
    cinquenta = cinquenta + 1

while valor >= 20:
    valor = valor - 20
    vinte = vinte + 1

while valor >= 5:
    valor = valor - 5
    cinco = cinco + 1

while valor >= 1:
    valor = valor - 1
    real = real + 1

if cinquenta > 0:
    print(f"Você receberá {cinquenta} nota(s) de R$50")

if vinte > 0:
    print(f"Você receberá {vinte} nota(s) de R$20")

if cinco > 0:
    print(f"Você receberá {cinco} nota(s) de R$5")

if real > 0:
    print(f"Você receberá {real} nota(s) de R$1")