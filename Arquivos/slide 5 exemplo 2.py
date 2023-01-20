#fatorial com for

num1 = int(input('Digite um número para saber seu fatorial: '))
fat = num1

if num1 < 0:
    print('ERRO. Número digitado deve ser maior ou igual a zero')
elif num1 == 0:
    print('O fatorial de zero é igual a 1')
else:
    for i in range (1,num1):
        fat = fat * (num1-i)

    print (f'O fatorial de {num1} é igual a {fat}')