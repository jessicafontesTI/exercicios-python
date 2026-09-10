n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1>n2:
    print(f'O \033[0;31;40mPRIMEIRO\033[m é maior ')

elif n2>n1:
    print(f'O \033[1;34mSEGUNDO\033[m é maior ')

elif n1 == n2:
    print(f'Os valores são \033[7;1mIGUAIS\033[m')