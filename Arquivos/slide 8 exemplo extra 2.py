N = int(input('Digite a quantidade de números: '))
while N <= 0:
    N = int(input('ERRO. Digite um número maior que zero para a quantidade de números: '))

rom = ''

for i in range (1,N+1):
    num = int(input(f'Digite o valor do {i}º número dentro do intervalo (0 : 4000): '))
    while num <= 0 and num >= 4000:
        num = int(input(f' ERRO. Digite o valor do {i}º número dentro do intervalo (0 : 4000): '))

    M = num // 1000
    romM = M * 'M'
    CM = (num % 1000) // 900
    romCM = CM * 'CM'
    D = ((num % 1000) % 900) // 500
    romD = D * 'D' 
    C = (((num % 1000) % 900) % 500) // 100
    romC = C * 'C'
    XC = ((((num % 1000) % 900) % 500) % 100) // 90
    romXC = XC*'XC'
    L = (((((num % 1000) % 900) % 500) % 100) % 90) // 50
    romL = L*'L'
    XL = ((((((num % 1000) % 900) % 500) % 100) % 90) % 50) // 40
    romXL = XL*'XL'
    X = (((((((num % 1000) % 900) % 500) % 100) % 90) % 50) % 40) // 10
    romX = X*'X'
    IX = ((((((((num % 1000) % 900) % 500) % 100) % 90) % 50) % 40) % 10 ) // 9
    romIX = IX*'IX'
    V = (((((((((num % 1000) % 900) % 500) % 100) % 90) % 50) % 40) % 10 ) % 9) // 5
    romV = V*'V'
    IV = ((((((((((num % 1000) % 900) % 500) % 100) % 90) % 50) % 40) % 10 ) % 9) % 5)//4
    romIV = IV*'IV'
    I = (((((((((((num % 1000) % 900) % 500) % 100) % 90) % 50) % 40) % 10 ) % 9) % 5)%4) // 1
    romI = I*'I'



    print (romM + romCM + romD + romC + romXC + romL + romXL + romX + romIX + romV + romIV + romI)