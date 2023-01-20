lista = []
lista2dig = []


num = int(input('Digite o primeiro número da sequência (negativo para parar): '))



while num >= 0:

    lista.append(num)
    num = int(input('Digite o próximo número da sequência (negativo para parar): '))
    



for i in range (len(lista)):
    if lista[i] >= 10 and lista[i] <= 99:
        lista2dig.append(lista[i])


print(lista2dig)

lista2dig.reverse()
print(lista2dig)

