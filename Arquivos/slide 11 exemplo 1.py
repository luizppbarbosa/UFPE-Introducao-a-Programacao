# calcular serie com n termos S = 37*38/1 - 36*37/2 + 35*36/3 - 32*34/4 + ...

def serie (n, num1 = 37, num2 = 38, den = 1):
    
    termo = (num1*num2)/den

    if den % 2 == 0:
        termo = - termo 
    
    if n > 1:
        termo = termo + serie(n-1,num1-1,num2-1,den+1)




    return termo




n = int(input('Digite a quantidade de termos da série: '))
while n <= 0 or n >= 37:
    n = int(input('ERRO. Digite a quantidade de termos positivo menor que 37: '))

soma = serie(n)

print(f'A soma da série com {n} termos é igual a {soma}')

    

