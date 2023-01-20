# calcular serie com n termos S = 1 + 3/2 + 5/3 + 7/4 ...

def serie(n, nu = 1, de = 1):
    
    s = nu/de
    
    if n > 1:
        s = s + serie(n-1,nu+2,de+1)
    return s



n = int(input('Digite a quantidade de termos da série: '))
while n <= 0:
    n = int(input('ERRO. Digite a quantidade de termos positiva: '))

soma = serie(n)

print(f'A soma da série com {n} termos é igual a {soma}')


