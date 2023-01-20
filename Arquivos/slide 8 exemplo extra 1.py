

n1 = int(input('Digite o primeiro número maior que zero: '))
while n1 <= 0:
    n1 = int(input('Digite o primeiro número maior que zero: '))
n2 = int(input('Digite o segundo número maior que zero: '))
while n2 <= 0:
    n2 = int(input('Digite o segundo número maior que zero: '))


divisoresn1 = []
divisoresn2 = []
divisorescomum = []

for i in range (1, n1+1):
    if n1 % i == 0:
        divisoresn1.append(i)

for i in range (1, n2+1):
    if n2 % i == 0:
        divisoresn2.append(i)

for i in divisoresn1:
    if i in divisoresn2:
        divisorescomum.append(i)

print (f' O MDC entre os números {n1} e {n2} é igual a {max(divisorescomum)}')
