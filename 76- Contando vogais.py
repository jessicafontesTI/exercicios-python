palavras = ('computador', 'python', 'programacao')

for palavra in palavras:
    c = 0
    vogais = ''

    for letra in palavra:
        if letra in 'aeiou':
            c = c + 1
            vogais = vogais + letra

    print(f'Na palavra {palavra} temos {c} vogais: {vogais}')