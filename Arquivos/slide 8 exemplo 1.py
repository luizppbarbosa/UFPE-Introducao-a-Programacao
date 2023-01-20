N = int(input('Digite o tamanho dos vetores a serem digitados: '))
while N < 1:
    N = int(input('ERRO. Digite um valor maior que zero para N: '))

vet1 = [0]*N
vet2 =  [0]*N
vet4 = [0]*N
cont = 1

for i  in range(N):
    vet1[i] = int(input(f'Digite o {cont} elemento do vetor 1: '))
    cont += 1

cont = 1
for i  in range(N):
    vet2[i] = int(input(f'Digite o {cont} elemento do vetor 2: '))
    cont += 1

vet3 = vet1 + vet2

for i in range(N):
    vet4[i] = vet1[i] + vet2[i]

print(f'O primeiro vetor digitado é: \n {vet1}')
print(f'O segundo vetor digitado é: \n {vet2}')
print(f'O vetor soma dos dois é : \n {vet3}')
print(f'O vetor soma dos dois é : \n {vet4}')