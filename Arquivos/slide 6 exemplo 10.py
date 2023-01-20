N = float(input('Digite o primeiro valor para calcular a média: (negativo para parar)'))

soma = 0
cont = 1

while N >= 0:
    soma += N
    media = soma / cont
    N = float(input('Digite o próximo valor para calcular a média: (negativo para parar)'))
    cont += 1


print (f'O valor da média dos números digitados é {media}')