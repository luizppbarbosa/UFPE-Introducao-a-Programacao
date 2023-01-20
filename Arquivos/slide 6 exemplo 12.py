# Ler um número inteiro e dizer se ele é primo ou não.

import math

n = int(input("Digite um número maior ou igual a 1: "))
while n < 1:
    n = int(input("Digite um número maior ou igual a 1: "))

raiz = int(math.sqrt(n))
i = 2
while (i <= raiz) and (n % i != 0):
    i += 1

if (i == raiz+1) and (n != 1):
    print(f"O número {n} é primo.")
else:
    print(f"O número {n} não é primo.")