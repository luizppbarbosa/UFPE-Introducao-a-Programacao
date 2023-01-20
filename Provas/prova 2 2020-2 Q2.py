

def serie (n, numi = 105, deni = 25, nump = 130, denp =35, aux = 1):

    if aux%2 == 0:
        soma = -nump/denp

    if aux%2 != 0:
        soma = numi/deni
    
    if n > 1:
        if aux%2 == 0:
            soma = soma + serie (n-1, numi, deni, nump+30, denp+20, aux+1)
        else:
            soma = soma + serie (n-1, numi+35, deni+20, nump, denp, aux+1)
    
    return soma


n = int(input('Digite a  quantiadde de termos da série: '))
while n <= 0:
    n = int(input('ERRO. Digite a  quantiadde de termos da série POSITIVA: '))

soma = serie(n)

print(f'A soma com {n} termos é igual a {soma}')


