# calcular valor da soma com n termos

N = int(input('Digite o valor de N: '))

num1 = 37
num2 = 38
soma = 0

for den in range (1,N+1):
    soma = ( ( num1 * num2 ) / den ) + soma
    num1 -= 1
    num2 -= 1

print (f'O valor da soma da série com {N} termos é igual a {soma}')

