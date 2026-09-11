import random

vitorias = 0

while True:

    pc = random.randint(1, 10)

    n = int(input("Digite um número: "))

    p = input("Seu número é PAR ou ÍMPAR? (P/I): ").upper().strip()[0]

    while p not in "PI":
        p = input("Opção inválida! Digite PAR ou ÍMPAR (P/I): ").upper().strip()[0]

    total = pc + n

    if total % 2 == 0:
        print(f"Você jogou {n} e o computador jogou {pc}.")
        print(f"O TOTAL foi {total} e deu PAR.")

        if p == "P":
            print("Parabéns, você VENCEU!")
            vitorias += 1
            print("Jogue novamente!")

        else:
            print("Você PERDEU!")
            break

    else:
        print(f"Você jogou {n} e o computador jogou {pc}.")
        print(f"O TOTAL foi {total} e deu ÍMPAR.")

        if p == "I":
            print("Parabéns, você VENCEU!")
            vitorias += 1
            print("Jogue novamente!")

        else:
            print("Você PERDEU!")
            break

print(f"GAME OVER! Você venceu {vitorias} vezes.")
    
