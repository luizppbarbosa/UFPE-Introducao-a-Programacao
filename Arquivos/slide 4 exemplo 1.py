num = int(input('Digite um número inteiro: '))

if num%2 == 0:
    res = num**2
    print(f'O valor digitado foi um número par, logo {num} ao quadrado é igual a {res}')
else:
    res = 5*num
    print(f'O valor digitado foi um número impar, logo {num} multiplicado por 5 é gual a {res}')
  