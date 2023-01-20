arq_velho = open('discipold.txt', 'r')
arq_novo = open('discipnew.txt', 'w')
tot_velho = tot_novo = disc_alteradas = 0

with arq_velho, arq_novo:
    for linha in arq_velho:
        tot_velho += 1
        codigo = linha[0:5]
        nome = linha[6:41]
        credito = linha[42:44]
        if (codigo != 'IF125') and (codigo != 'IF380'):
            tot_novo += 1
            if codigo[0:2] == 'MA':
                disc_alteradas += 1
                credito = '5'
            carga = int(credito) * 15
            arq_novo.write(f'{codigo} {nome} {credito:2} {str(carga):3}\n')