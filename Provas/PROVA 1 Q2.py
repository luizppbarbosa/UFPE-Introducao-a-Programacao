print('Daremos início a digitação de números inteiros! ')

cont = 0
cont3dig = 0
soma3dig = 0
lista = []
lista3digneg = []
lista3digpos =[]

num = int(input('Digite o primeiro número inteiro: (-9999999999 para parar a digitação) '))

while num == -9999999999:
    num = int(input('Digite pelo menos um número inteiro válido: '))

while num != -9999999999 and cont < 400:
    lista.append(num)

    num = int(input('Digite o próximo número inteiro, -9999999999 para parar: '))
    
    cont += 1

if cont == 400:
    print('número máximo de valores atingido, o último número digitado será descartado')

print(f'A quantidade total de números lidos é igual a {cont} \n')

for i in lista:
    if i <= -100 and i >= -999: 
        lista3digneg.append(i)
        soma3dig += i
        cont3dig += 1
    if i >= 100 and i <= 999:
        lista3digpos.append(i) 
        soma3dig += i
        cont3dig += 1
    

print('Os números digitados com 3 dígitos significativos na ordem em que foram lidos, com os negativos primeiro do que os positivos são: \n')
lista3digneg.extend(lista3digpos)
print(f'{lista3digneg} \n')

med = soma3dig / cont3dig

print(f'A média aritimética de todos os números de 3 dígitos é igual a {med}')