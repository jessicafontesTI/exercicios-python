n = 0
s = 0
t = 0

while True:
    n = int(input("Digite um valor ou 999 para parar: "))

    if n != 999:
        s = s + n
        t = t + 1

    if n == 999:
        break

print(f"Foram digitados {t} números e a soma deles é {s}")
