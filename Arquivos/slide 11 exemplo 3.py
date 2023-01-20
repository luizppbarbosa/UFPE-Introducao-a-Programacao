
def fib(num):

    if num == 0:
        termo = 0
    elif num == 1:
        termo = 1
    else:
        termo = fib(num-1) + fib(num-2)
    
    return termo



lista = []

num = int(input('Digite o pirmeiro número: '))
while num <= 0:
    num = int(input('ERRO. Digite pelo menos um número válido: '))

while num > 0:

    lista.append(num)

    num = int(input('Digite o próximo número: '))

print(lista)

for i in lista:
    print(f'O termo {i} da sequência de Fibonacci é {fib(i)}')
