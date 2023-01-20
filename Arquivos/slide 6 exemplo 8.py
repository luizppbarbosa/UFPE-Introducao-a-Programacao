
N = int(input('Digite o valor de N: '))
num1 = 37
num2 = 38
den = 1
soma = 0

while den <= N:
    soma += (num1*num2)/den
    num1 -= 1
    num2 -= 1
    den += 1

print(f'A soma dos {N} números da série é igual a {soma}')


