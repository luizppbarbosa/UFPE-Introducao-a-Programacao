
N = int(input('Digite o primeiro número da série. zero para parar a digitação: '))
min = N

while N != 0:
    N = int(input('Digite o próximo número da série. zero para parar a digitação: '))
    if N < min and N != 0:
        min = N
    
print (f'O menor número digitado é {min}')
