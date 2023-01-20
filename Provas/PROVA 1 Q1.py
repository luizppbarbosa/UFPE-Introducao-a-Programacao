
qtd = int(input('Digite a quantidade de vezes que deseja calcular a série: '))
while qtd <=0:
    qtd = int(input('ERRO. Digite um número maior que zero para a quantidade de vezes que deseja calcular a série: '))

for i in range(1,qtd+1):
    n = int(input(f'Digite a quantidade de termos da série para a soma número {i}: '))
    while n <=0:
        n = int(input(f'ERRO. Digite a quantidade de termos da série maior que zero para a soma número {i}: '))
    
    num1 = 10
    den1 = 1
    num2 = 12
    den2 = 5
    soma = 0


    for j in range (1,n+1):
        if j % 2 != 0:
            soma += num1/den1
            num1 += 4
            den1 += 7
        else:
            soma -= num2/den2
            num2 += 4
            den2 += 6
    print (f'A soma com {n} termos é igual a {round(soma, 2)}')