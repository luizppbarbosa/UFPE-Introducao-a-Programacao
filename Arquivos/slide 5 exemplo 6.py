# tabela de conversão F pra C

inf = int(input('Digite o limite inferior: '))
sup = int(input('Digite o limite superior: '))

if inf > sup:
    inf, sup = sup, inf

for faren in range (inf, sup+1):
    celcius = ((faren-32) * 5) / 9
    print(f'F = {faren}     C = {celcius}')