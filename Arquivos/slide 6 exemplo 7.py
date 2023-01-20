# ler N e imprimir N-ésimo termo da sequência

N = int(input('Digite o valor de N: '))
cont = 1
termo = -1
incr = 1

while N <= 0:
    N = int(input('ERRO. Digite o valor de N maior que zero: '))

while cont < N:
    termo += incr  

    if incr == 1:
        incr = 5
    else:
        incr = 1
    
    cont += 1

print (f'O valor do termo {N} da sequência é igual a {termo}')
