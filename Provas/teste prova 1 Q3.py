# leitura dos dados

 

tabela = {}

qtdcpf = 0

 

cpf = int(input('Digite o CPF do funcionário: '))

while cpf <= 0:

    cpf = int(input('ERRO. Digite pelo menos um CPF maior que zero: '))

 

while cpf != 0 and qtdcpf < 250:

    nome = str(input('Digite o nome do funcionário: '))

    genero = str(input('Digite o gênero do funcioário: ( M ou F ) '))

    while genero != 'M' and genero != 'F':

        genero = str(input('ERRO. Digite o gênero do funcioário: ( M ou F ) '))

    dep = int(input('Digite a quantidade de dependentes do funcionário: (>= 0)'))

    while dep < 0:

        dep = int(input('ERRO. Digite a quantidade de dependentes do funcionário: (>= 0)'))

    tabela[cpf] = (nome,genero,dep)

 

    cpf = int(input('Digite o CPF do próximo funcionário: (zero para parar)'))

    while cpf < 0:

        cpf = int(input('ERRO. CPF não pode ser negativo, digite zero para parar: '))

   

    qtdcpf += 1

 

if qtdcpf == 250:

    print('Número máximo de funcionários atingido, o último número digitado foi descartado! ')

print(tabela)

# consulta de dados

 

genero = str(input('Digite o gênero da consulta: '))

while genero != 'M' and genero != 'F':

    genero = str(input('ERRO. Digite o gênero do funcioário: ( M ou F ) '))

 

dep = int(input('Digite a quantidade de dependentes da consulta: '))

while dep < 0:

    dep = int(input('ERRO. Digite a quantidade de dependentes do funcionário: (>= 0)'))

 

print(f'As pessoas do gênero {genero} com pelo menos {dep} dependentes são: \n')

 

qtd = 0

for i in tabela:

    if tabela[i][1] == genero and tabela[i][2] >= dep:

        print(f' O funcionário {tabela[i][0]} tem {tabela[i][2]} dependentes')

        qtd += 1

 

print(f'A quantidade de pessoas selecionadas é igual a {qtd}')

 

qtddep = 0

for i in tabela:

    if  tabela[i][2] >= dep*2:

        qtddep += 1

   

print(f'{qtddep} pessoas tem pelo menos o dobro da quantidade de dependentes informado!')

 

print(f' A quantidade de pessoas cadastradas é igual a {len(tabela)}')