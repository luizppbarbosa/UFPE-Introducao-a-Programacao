fim = False
while not fim:
    try:
        def calculaTotal (linha):

            qtd1 = int(linha [0:2])
            val1 = float(linha [3:9])
            qtd2 = int(linha [10:12])
            val2 = float(linha [13:19])
            qtd3 = int(linha [20:22])
            val3 = float(linha [23:29])
            qtd4 = int(linha [30:32])
            val4 = float(linha [33:39])

            valortot = qtd1*val1 + qtd2*val2 + qtd3*val3 + qtd4*val4

            return valortot



        nome = input('Qual o nome do arquivo a ser gravado? ')
        formato = int(input('Qual o formato do arquivo a ser gravado? \n1=texto-simples ou 2=texto-csv: '))
        while formato != 1 and formato != 2:
            formato = int(input('ERRO. Formato deve ser 1=texto-simples ou 2=texto-csv'))

        if formato == 1:
            tipo = '.txt'
        else:
            tipo = '.csv'

        cont = 0
        faturamento = 0

        leitura = open ('comprasClientes.txt','r')
        escrita = open (nome+tipo, 'w')

        with leitura, escrita:
            for linha in leitura:
                codcompra = linha [0:5]
                codcliente = linha [6:10]

                total = calculaTotal (linha[11:50])

                if formato == 1: 
                    escrita.write(f'{codcompra} {codcliente} {round(total,2)}\n')
                else:
                    escrita.write(f'{codcompra};{codcliente};{round(total,2)}\n')

                cont += 1
                faturamento += total
            
        

    except ValueError:
        print('ERRO, valor inconsistente digitado! ')

    except PermissionError:
        print('Usuário sem acesso ao local de escrita! ')
        fim = True

    except FileNotFoundError:
        print('Arquivo inexistente! ')
        fim = True


    else:
        print(f'{cont} registros foram gravados no arquivo')
        print(f'O faturamento total da loja foi igual a {faturamento}')
        fim = True
