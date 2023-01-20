def preenchetab():
    n = int(input('Digite a quantidade de profissões a serem digitadas: '))
    while n <= 0:
         n = int(input('ERRO. Digite um valor positivo para a quantidade de profissões a serem digitadas: '))
    tab = {}

    for i in range (n):
        cod = int(input('Digite o código da profissão: '))
        while cod <= 0:
            cod = int(input('ERRO. Digite um número positivo para o código da profissão: '))
        nome = str(input('Digite o nome da profissão: '))
        area = str(input('Digite a área da profissão: '))
        tab[cod] = (nome,area) 
    return (tab)


print('Programa teste de função de preencher tabela!')

tabela = preenchetab()
print(tabela)


cod = int(input('Digite o código para buscar a profissão: '))
while cod > 0:
    if cod in tabela:
        print(f'O código {cod} é referente a profissão {tabela[cod][0]} da área {tabela[cod][1]}')
    else:
        print(f'O código {cod} não existe na tabela! ')

    cod = int(input('Digite o próximo código da consulta: '))

print('Número de código inválido digitado, fim do programa!')