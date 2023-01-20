# Somar inteiros ímperes entre um intervalo fornecido

inf = int(input('Digite o intervalo inferior: '))
sup = int(input('Digite o intervalo superior: '))
soma = 0
cont = 0

if inf > sup:
    inf, sup = sup, inf

for i in range (inf, sup+1):
    if i % 2 != 0:
        soma += i
        cont += 1

print(f'A soma dos {cont} inteiros ímpares entre {inf} e {sup} é igual a {soma}')