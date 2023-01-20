

def serie (n, numi = 105, nump = 130, den = 25, aux = 1):

    if aux % 2 != 0:
        soma = numi/den
    else:
        soma = -nump/den

    if n > 1:
        if aux % 2 != 0:
            soma = soma + serie (n-1, numi+35, nump, den+10, aux+1)
        else:
            soma = soma + serie (n-1, numi, nump+30, den+10, aux+1)
    
    return soma



n = int(input('Digite a quantidade de termos da soma:'))
while n <= 0:
    n = int(input('ERRO. Digite a quantidade de termos POSITIVA:'))

res = serie(n)

print (f'O resultado da série com {n} termos é igual a {res}')
