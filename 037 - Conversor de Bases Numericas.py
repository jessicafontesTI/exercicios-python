numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases de conversão:\n [ 1 ] converter para Binário\n [ 2 ] converter para Octal\n [ 3 ] converter para Hexadecimal' )
escolha = int(input('Sua opção: '))
if escolha == 1:
    print(f'O número em Binário é {bin(numero)[2:]})')
elif escolha == 2:
    print(f'O número em Octal é {oct(numero)[2:]}')
elif escolha == 3:
    print(f'O número em Hexadecimal é {hex(numero)[2:]}')
else:
    print('Opção inválida')