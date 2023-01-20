# ler N e impirmir N-ésimo termo da sequencia


N = int(input('Digite o valor de N: '))
incr = 1
termo = -1

if N <= 0:
    print('ERRO. N deve ser maior que zero')
else:
    for i in range (2, N+1):
        termo += incr
        if incr == 1:
            incr = 5
        else: 
            incr = 1

    print(f'O {N} termo é igual a {termo}')


