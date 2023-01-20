# calcular soma da série com N termos

N = int(input('Digite a quantidade de termos da série: '))
num = 2
den = 500
div = 0

if N >= 0 and N < 50:
    for i in range (1,N+1):
        div = div + (num/den)
        den -= 10
        if num == 2:
            num = -5
        else:
            num = 2

    print (f'A soma dos {N} primeiros números da série é igual a {div}')
else:
    print('ERRO. N digitado fora do intervalo aceito')