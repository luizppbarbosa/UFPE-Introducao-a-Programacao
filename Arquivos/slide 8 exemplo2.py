N = int(input('Digite o valor do tamanho da lista a  ser digitada: '))

while N < 1:
    N = int(input('ERRO. Digite um valor maior que zero para N: '))


vet = [0]*N
vetpar = [0]*N
vetimpar = [0]*N
cont = 1
contp = 0
conti = 0

for i  in range (N):
    vet[i] = int(input(f'Digite o {cont} elemento da lista: '))
    cont += 1

    if vet[i] % 2 == 0:
        vetpar[contp] = vet[i]
        contp += 1
    else:
        vetimpar[conti] = vet[i]
        conti += 1

par = vetpar[:contp]
impar = vetimpar[:conti]
print (f'A lista digitada foi: \n {vet}')
print (f'Os elementos pares da lista são: \n {par}')
print (f'Os elementos impares da lista são: \n {impar}')