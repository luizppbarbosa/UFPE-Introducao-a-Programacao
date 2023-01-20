try:

    def lecentros (tab):
        with open ('centros.txt','r') as leitura:
            for linha in leitura:
                cod = linha[0:3]
                centro = linha[4:29]
                tab[cod] = centro

    def achanome(codigo):
        with open ('centros.txt','r') as leitura:
            for linha in leitura:
                cod = linha[0:3]
                centro = linha[4:30]
                if codigo == cod:
                    nomecentro = centro
        return nomecentro

    tabela = {}
    lecentros(tabela)
    cont1 = 0


    leitura2 = open ('discip.txt','r')
    escrita = open ('discipCompleto.txt','w')

    with leitura2, escrita:
        for linha in leitura2:
            cont1 += 1
            cod = linha[0:5]
            nome = linha [6:41]
            cred = linha [42:44]
            codcen = linha [45:48]
            for i in tabela:
            
                if codcen == i:
                    centro = tabela[i]
            escrita.write(f'{cod} {nome} {cred} {codcen} {centro}\n')
        

 

except PermissionError:
    print('Usuário sem permissão para acessar o diretório de escrita! ')

except FileNotFoundError:
    print('Arquivo não encontrado! ')

else:
       print(f'Existem {cont1} disciplinas e {len(tabela)} centros')
