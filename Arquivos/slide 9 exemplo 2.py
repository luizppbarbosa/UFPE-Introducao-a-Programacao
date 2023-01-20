# preenchimento da tabela

lista = {}

cod = int(input('Digite o valor do código: '))
while cod <= 0:
    cod = int(input('ERRO> Digite pelo menos um código: '))

while cod > 0:
    nome = str(input('Digite o nome: '))
    salario = float(input('Digite o salário: '))
    while salario <= 0:
        salario = float(input('ERRO. Digite um valor positivo para o salário: '))
    lista[cod] = (nome,salario)
    cod = int(input('Digite o próximo código: '))
    

print(lista)
print('Fim da leitura de dados! ')
print('Início da consulta de dados! ')

#leitura da tabela

salario = float(input('Digite o valor máximo de salário: '))
while salario <= 0:
    salario = float(input('ERRO. Digite um valor positivo para o máximo de salário: '))

while salario > 0:
    qtd = 0
    saltot = 0
    print (f'As pessoas com salário menor do que {salario} são: ')
    for i in lista:
        if lista[i][1] < salario:
            print(f'O salário de {lista[i][0]} é R${lista[i][1]}')
            qtd += 1
            saltot += lista[i][1]
    print(f'Temos {qtd} pessoas com salário abaixo do salário digitado! ')
    if qtd == 0:
        med = 0
    else:
        med = saltot / qtd
    print(f'A média de seus salários é igual a R${med}')

    salario = float(input('Digite o próximo valor de salário máximo: '))

print ('Fim do programa! ')