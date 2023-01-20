
def CalculaS (n, num = 1, deni = 2, denp = 4, aux = 1):
    if aux % 2 != 0:
        soma = num / deni
    else:
        soma = - num / denp

    if n > 1:
        if aux % 2 != 0:
            soma = soma + CalculaS (n-1, num*3, deni*2, denp, aux+1)
        else:
            soma = soma + CalculaS (n-1, num*3, deni, denp+5, aux+1)
        
    return soma

def Imprime (lista):
    for i in lista:
        res = CalculaS(i)
        print(f'O resultado de S com {i} termos é {round(res,3)}')


num = int(input('Digite a primeira quantidade de termos para calcular a soma: '))
while num <= 0:
    num = int(input('ERRO. Digite pelo menos um valor positivo: '))


lista = []

while num > 0:
    lista.append(num)
    num = int(input('Digite a próxima quantidade de termos para calcular a soma: '))

lista.sort(reverse=True)

print('Número de termos inválido digitado!')
print(f'O usuário solicitou {len(lista)} cálculos')

Imprime(lista)