lista = [0]*4
lista2dig = [0]*4
cont = 0
cont2dig = 0


num = int(input('Digite o primeiro número da sequência (negativo para parar): '))



while num >= 0 and cont < 4:
    
    lista[cont] = num
    cont += 1
    num = int(input('Digite o próximo número da sequência (negativo para parar): '))

if cont == 4:
    print('Número máximo de números atingido, a último número digitado foi descartado! ') 

if cont == 0 and num < 0:
    print('Nenhum número positivo foi digitado! ')
else:

    for i in range (len(lista)):
        if lista[i] >= 10 and lista[i] <= 99:
            lista2dig[cont2dig] = lista[i]
            cont2dig += 1


    #print(lista2dig)
    lista2dig = lista2dig[:cont2dig]
    lista2dig.reverse()
    print(lista2dig)