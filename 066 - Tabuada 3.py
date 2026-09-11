n = 0
while True:
    n = int(input("Você quer ver a tabuada de qual valor? "))
    t1 = 1*n
    t2 = 2*n 
    t3= 3*n
    t4 = 4*n
    t5 = 5*n
    t6 = 6*n
    t7 = 7*n
    t8 = 8*n
    t9 = 9*n
    t10 = 10*n
    print (f' 1 * {n} = {t1}\n 2 * {n} = {t2}\n 3 * {n} = {t3}\n 4 * {n} = {t4}\n 5 * {n} = {t5}\n 6 * {n} = {t6}\n 7 * {n} = {t7}\n 8 * {n} = {t8}\n 9 * {n} = {t9}\n10 * {n} = {t10}\n')
    if n < 0:
        break
print("O programa encerrou!")
