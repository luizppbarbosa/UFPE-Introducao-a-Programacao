
fim = False
while not fim:
    try:

        def calculaCompra (estmin, estat):

            if estat < estmin*0.5:
                qtdCompra = estmin*1.2 - estat
            elif estat <= estmin*0.9:
                qtdCompra = estmin*1.1 - estat
            else:
                qtdCompra = estmin - estat
                if qtdCompra < 0:
                    qtdCompra = 0

            return int(qtdCompra)


        arq = input('Digite o nome do arquivo: ')

        leitura = open (arq,'r')
        escrita = open ('compras.txt','w')

        with leitura, escrita:
            for linha in leitura:
                cod = linha[0:3]
                nome = linha[4:24]
                qtdmin = linha[25:29]
                qtdat = linha[30:34]
                qtdCompra = calculaCompra(int(qtdmin), int(qtdat))
                escrita.write(f'{cod} {nome} {qtdCompra}\n')

    except FileNotFoundError:
        print('Arquivo não encontrado! ')

    except PermissionError:
        print('Usuário sem permissão de escrita para o diretório! ')
        fim = True

    else:
        print('FIM DO PROGRAMA! ')
        fim = True
