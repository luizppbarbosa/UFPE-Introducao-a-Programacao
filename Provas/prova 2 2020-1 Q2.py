
def fatorial(n):

    if n == 0 or n ==1:
        fat = 1

    elif n > 1:
        fat = n * fatorial (n-1)
    
    return fat


def serie (n, numi = 3, nump = 5, den = 1):

    if den % 2 != 0:
        soma = numi/fatorial(den)
    else:
        soma = nump/fatorial(den)
    
    if n > 1:
        if den % 2 != 0:
            soma = soma + serie (n-1, numi * 5, nump, den+1)
        else:
            soma = soma + serie (n-1, numi, nump * 6, den+1)


    return soma


n = int(input('Digite a quantidade de termos da soma: '))
while n <= 0:
    n = int(input('ERRO. Digite a quantidade de termos POSITIVA: '))

soma = serie (n)

print(soma)
