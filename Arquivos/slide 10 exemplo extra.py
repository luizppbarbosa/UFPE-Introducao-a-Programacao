# Faça um programa que recebe do usuário uma lista de inteiros com tamanho N (também defindo pelo usuário).
# Em seguida, escreva uma função que recebe essa lista como parâmetro e retorna uma outra
# lista (possivelmente menor) sem conter elementos repetidos.

def retirarep(lista):
    listarep = []
    for i in lista:
        if i not in listarep:
            listarep.append(i)
    return listarep



n = int(input('Digite a quantidade de termos da lista: '))

lista1 = []


for i in range (1, n+1):
    lista1.append(int(input(f'Digite o {i}º número da lista: ')))

print(lista1)

lista2 = retirarep(lista1)

print(lista2)