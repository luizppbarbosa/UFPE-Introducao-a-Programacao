
def serie (n, numi = 2, deni = 1, nump = 7, denp =5, aux = 1):

    if aux%2 == 0:
        soma = -nump/denp

    if aux%2 != 0:
        soma = numi/deni
    
    if n > 1:
        if aux%2 == 0:
            soma = soma + serie (n-1, numi, deni, nump+6, denp+4, aux+1)
        else:
            soma = soma + serie (n-1, numi*4, deni*3, nump, denp, aux+1)
    
    return soma


n = int(input('Digite a  quantiadde de termos da série: '))
while n <= 0:
    n = int(input('ERRO. Digite a  quantiadde de termos da série POSITIVA: '))

soma = serie(n)

print(f'A soma com {n} termos é igual a {soma}')