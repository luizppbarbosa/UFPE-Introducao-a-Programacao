N = int(input('Digite a quantidade de profissões a serem digitadas: '))

prof = {}

for i in range (N):
    cod = int(input('Digite o código da profissão: '))
    while cod < 1:
        cod = int(input('ERRO. Digite o código da profissão: '))
    nome = str(input('Digite o nome da profissão: '))
    area = str(input('Digite a área da profissão: '))
    prof[cod] = (nome,area)


cod = int(input('Digite o código: '))

while cod >= 0:
    if cod in prof:
        nome, area = prof[cod]
        print(f'O código {cod} é referente a profissão {nome} da área {area}')
    else:
        print(f'O código {cod} não existe na tabela! \n')
    cod = int(input('Digite o próximo código: '))

print('Valor de código menor ou igual a zero digitado. Fim do programa')