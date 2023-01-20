# tabela fahrenheit while

inf = int(input('Digite o valor do limite inferior do intervalo: '))
sup = int(input('Digite o valor do limite superior do intervalo: '))
celcius = 0

if inf > sup:
    inf, sup = sup, inf

far = inf

while far <= sup:
    celcius = ((far-32)*5)/9

    print (f'Fahrenheit = {far}  --->  Celcius = {celcius}')

    far += 1

