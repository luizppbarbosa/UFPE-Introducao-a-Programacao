

def serie(n, num = 2, den = 500):

    soma = num/den

    if num % 2 != 0:
        soma = -soma
    
    if n > 1:
        if num%2 == 0: 
            soma = soma + serie(n-1, 5, den-10)
        else:
            soma = soma + serie(n-1, 2, den-10)
    
    return soma






n = int(input('Digite a quantidade de termos para calcular a série: '))
while n <= 0 or n >= 50:
    n = int(input('ERRO. Digite a quantidade de termos POSITIVA e menor que 50: '))

soma = serie(n)

print(f'O resultado da série com {n} números é igual a {soma}')
