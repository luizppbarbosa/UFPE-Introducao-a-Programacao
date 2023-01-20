n1 = int(input('Digite o primeiro número:'))
while n1 <= 0:
    n1 = int(input('ERRO. Digite o primeiro número (POSITIVO):'))

n2 = int(input('Digite o segundo número: '))
while n2 <= 0:
    n2 = int(input('ERRO. Digite o segundo número (POSITIVO):'))

div1 = n1
div2 = n2
cont = 2
mmc = 1

while div1 > 1 or div2 > 1:
    while div1 % cont == 0 or div2 % cont == 0:
        if div1 % cont == 0:
            div1 = div1/cont
        if div2 % cont == 0:    
            div2 = div2/cont
        mmc *= cont
    cont += 1        

print(f'O MMC entre {n1} e {n2} é igual a {mmc}')

