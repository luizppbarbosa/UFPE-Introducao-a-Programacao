def serie(n, num = 150, deni = 4, denp = 9, cont = 1):

    if n <= 0:
        soma = 0
    else:
        if cont%2 != 0:
            soma = num/deni
        else:
            soma = -num/denp

    if n > 1:
        if cont%2 != 0:
            soma = soma + serie (n-1, num-5, deni+2, denp, cont+1)
        else:
            soma = soma + serie (n-1, num-5, deni, denp+4, cont+1)


    return soma 


n = int(input('Digite a quantidade de termos da soma: (<=0 PARA)'))

while n > 0:
    soma = serie(n)

    print(f'A série com {n} termos totaliza {round(soma,3)}')
    n = int(input('Digite a quantidade de termos da soma: (<=0 PARA)'))

print('Condição de parada digitada!')