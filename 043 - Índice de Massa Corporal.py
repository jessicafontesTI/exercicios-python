altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

calculo = peso / (altura * altura) 

if calculo <= 18:
    print(f'Seu IMC é {calculo:.2f} você está abaixo do peso')
elif calculo > 18 and calculo <= 25:
    print(f'Seu IMC é {calculo:.2f} você está no peso normal')
elif calculo > 25 and calculo <= 30:
    print(f'Seu IMC {calculo:.2f} você está acima do peso')
elif calculo > 30 and calculo <= 35:
    print(f'Seu IMC é {calculo:.2f} você tem obesidade grau I')
elif calculo > 35 and calculo <= 39:
    print(f'Seu IMC {calculo:.2f} e você tem obesidade grau II')
else:
    print(f'Seu IMC {calculo:.2f} e você tem obesidade grau III')