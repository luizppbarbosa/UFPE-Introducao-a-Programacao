#preenchimento da tabela

tabela = {}
qtdcod = 0


cod = str(input('Digite o código de 5 caracteres da disciplina: \n'))
while len(cod) != 5:
    cod = str(input('ERRO. O código da disciplina precisa ter 5 caracteres: \n'))

while cod != 'FIM' and qtdcod < 500:
    nome = str(input('Digite o nome da disciplina: '))
    carh = int(input('Digite a carga horária da disciplina: '))
    while carh <= 0:
        carh = int(input('ERRO. Digite valor positivo para a carga horária da disciplina: '))
    cred = int(input('Digite o número de créditos da disciplina: '))
    while cred <= 0:
        cred = int(input('ERRO. Digite valor positivo para o número de créditos da disciplina: '))
    tabela[cod] = (nome,carh,cred)
    cod = str(input('Digite o próximo código de 5 caracteres da disciplina: \n'))
    while len(cod) != 5 and cod != 'FIM':
        cod = str(input('ERRO. O código da disciplina precisa ter 5 caracteres: \n'))
    qtdcod += 1

if qtdcod == 500:
    print('Número máximo de disciplinas atingido, o último número digitado foi descartado! ') 

print (tabela)

# leitura da tabela

cod = str(input('Digite o prefixo da disciplina: '))
while len(cod) > 4:
    cod = str(input('ERRO. O prfixo tem no máximo 4 digitos: '))


qtd = 0
carhtot = 0
print(f'As disciplinas com o prefixo {cod} são: \n')
for i in tabela:
    if cod == i [:len(cod)]:
        print(f'{tabela[i][0]} com {tabela[i][1]} horas e {tabela[i][2]} créditos')
        qtd += 1
        carhtot += tabela[i][1]



if qtd == 0:
    print('Não possui nenhuma disciplina com esse prefixo! ')    
else:
    med = carhtot / qtd
    print(f'A média das cargas horárias das {qtd} disciplinas com o mesmo prefixo digitado é igual a {med}')

