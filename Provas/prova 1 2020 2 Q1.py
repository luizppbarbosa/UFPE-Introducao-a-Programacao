n = int(input('Digite a quantidade de termos da série: '))
while n < 1:
    n = int(input('ERRO. Digite uma quantidade de termos positiva: '))

num1 = 2
den1 = 1
num2 = 7
den2 = 5
soma = 0


for i in range (1,n+1):
    if i % 2 != 0:
        soma += num1/den1
        num1 *= 4
        den1 *= 3
    else:
        soma -= num2/den2
        num2 += 6
        den2 += 4
   
print (f'O valor da série com {n} termos é {round(soma, 4)}')









