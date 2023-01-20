
def leitura():
    tab = {}
    with open ('discipold.txt', 'r') as leitura:
        for linha in leitura:
            cod = linha [0:5]
            nome = linha [6:41]
            cred = linha [42:44]

            tab[cod]=[nome,int(cred)]
    
    return tab

try:

    tabela = leitura()
    cont1 = 0
    cont2 = 0
    cont3 = 0


    with open ('discipnew.txt', 'w') as escrita:

        for i in tabela:

        
            if i[0:2] == 'MA':
                tabela[i][1] = 5
                cont2 += 1
            if i != 'IF125' and i != 'IF380':
                escrita.write(f'{i} {tabela[i][0]} {tabela[i][1]:2}  {(tabela[i][1]*15):3}\n')
                cont3 += 1
            cont1 += 1

    

except FileNotFoundError:
    print('Arquivo não encontrado! ')
except PermissionError:
    print('Usuário sem acesso ao diretório! ')
else:
    print(f'O número de disciplinas no arquivo antigo é {cont1}.\nO número de disciplinas no arquivo novo é {cont3}.\n{cont2} Disciplinas tiveram seus créditos alterados! ')

        