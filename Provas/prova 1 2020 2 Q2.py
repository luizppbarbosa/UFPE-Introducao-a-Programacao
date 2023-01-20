print('Daremos início a digitação de números inteiros negativos! ')

cont = 0
lista = []
lista1 = []
lista2 = []

num = int(input('Digite o primeiro número negativo: (<0) '))

while num >= 0:
    num = int(input('Digite pelo menos um número negativo: '))


while num != 0 and cont < 150:
    lista.append(num)

    num = int(input('Digite o próximo número negativo, zero para parar: '))
    while num > 0:
        num = int(input('ERRO. o número precisa ser negativo, zero para parar: '))
    cont += 1

if cont == 150:
    print('número máximo de valores atingido, o último número digitado será descartado')

for i in lista:
    if i <= -10 and i >= -99 and i%5 == 0: 
        lista1.append(i)

for i in lista:
    if i%7 != 0:
        lista2.append(i)



lista1.reverse()

if len(lista1) == 0:
    print('Nenhum múltiplo de 5 com 2 dígitos foi digitado! ')
else: 
    print(lista1)


if len(lista2) == 0:
    print('Nenhum não multiplo de 7 foi digitado! ')
else:
    print(max(lista2))