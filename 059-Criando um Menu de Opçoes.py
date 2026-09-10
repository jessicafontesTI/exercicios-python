primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))

menu = 0

while menu != 5:

        menu = int(input('''
    >>>> MENU <<<<
    [1] SOMAR
    [2] MULTIPLICAR
    [3] QUAL É O MAIOR?
    [4] NOVOS NÚMEROS
    [5] SAIR
    >> '''))

        if menu == 1:
            soma = primeiro + segundo
            print(f'A soma de {primeiro} + {segundo} é igual a {soma}')

        elif menu == 2:
            multiplicacao = primeiro * segundo
            print(f'A multiplicação de {primeiro} x {segundo} é igual a {multiplicacao}')

        elif menu == 3:
            if primeiro > segundo:
                print(f'O maior número é {primeiro}')
            elif segundo > primeiro:
                print(f'O maior número é {segundo}')
            else:
                print('Os dois números são iguais.')

        elif menu == 4:
            primeiro = int(input('Digite o primeiro valor: '))
            segundo = int(input('Digite o segundo valor: '))

        elif menu == 5:
            print('Finalizando o programa...')

        else:
            print('Opção inválida! Tente novamente.')

print('FIM DO PROGRAMA!')