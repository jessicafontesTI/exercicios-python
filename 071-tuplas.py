numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove', 'dez', 'onze', 'doze', 'treze', 'quatroze', 'quinze', 'dezesseis','dezessete', 'dezoito', 'dezenove', 'vinte'
)

d = int(input('Digite um valor entre 0 e 20: '))

while d < 0 or d > 20:
    d = int(input('Inválido! Escolha um número entre 0 e 20: '))

print(f'Você digitou o número {numero[d]}.')
