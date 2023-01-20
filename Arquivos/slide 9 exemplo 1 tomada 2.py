tabela = {}
cont = 0
qtd = 0

# criação do dicionário

cod = int(input('Digite o código do curso : '))

while cod <= 0:
    cod = int(input('ERRO. Digite pelo menos um código de curso válido: '))

while cod != 0:
    nome = str(input('Digite o nome do curso: '))
    centro = int(input('Digite o número do centro: '))
    while centro <= 0:
        centro = int(input('ERRO. Digite um número de centro maior que zero: '))
    tabela[cod] = (nome,centro)
    cod = int(input('Digite o próximo código do curso: '))
    while cod < 0:
        cod = int(input('ERRO. Digite o próximo código do curso válido: '))
    cont += 1

print(tabela)
print(len(tabela))


# leitura do dicionário

centro = int(input('Digite o código do centro para saber os cursos associados a ele: '))


while centro >= 0:
    print(f'Os cursos do centro {centro} são: ')
    qtd = 0
    for i in tabela:
        if tabela[i][1] == centro:
            print(tabela[i][0])
            qtd += 1
    if qtd == 0:
        print('Nenhum curso cadastrado neste centro!')
    centro = int(input('Digite o próximo código de centro (<=0 para parar): '))





print('Fim do programa!')