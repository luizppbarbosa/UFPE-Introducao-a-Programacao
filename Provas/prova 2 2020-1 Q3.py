# TIPO PROCEDIMENTO!!



def MelhoresClientes (NomeEmpresa, pontmin):
    leitura = open(f'{NomeEmpresa}.txt','r')
    escrita = open(f'Melhores {NomeEmpresa}.txt', 'w')

    cont = 0
    soma = 0
    with leitura, escrita:
        for linha in leitura:
            matricula = linha [0:5]
            sexo = linha [6:7]
            pontos = linha [8:15]
            cliente = linha [16:51]
                    
            if int(pontos) > pontmin:
                escrita.write(f'{matricula} {pontos}\n')
                cont += 1
                soma += int(pontos)

        media = soma / cont

        print(f'Empresa {NomeEmpresa}')
        print(f'Foram gravados {cont} registros no arquivo \'Melhores {NomeEmpresa}\'')
        print(f'A média das pontuações dos melhores clientes é {media}')

fim = False
while not fim:
    try:
        n = int(input('Quantas empresas serão analisadas? '))
        while n <= 0:
            n = int(input('ERRO. Quantidade de empresas precisa ser positiva! '))
    except ValueError:
        print('Valor inconsistente digitado! ')
    else:
        fim = True

        
for i in range (1, n+1):

    fim = False
    while not fim:
        try:
            NomeEmpresa = input(f'Digite o nome da {i}ª empresa: ')
            pontmin = int(input('Digite a quantidade de pontos necessários na escolha dos clientes: '))
            MelhoresClientes(NomeEmpresa, pontmin)
        except FileNotFoundError:
            print ('Arquivo não encontrado! ')
            fim = True
        except PermissionError:
            print ('Usuário sem permissão para este diretório! ')
            fim = True
        except ValueError:
            print ('Valor inconsistente digitado para a pontuação mínima! ')
        else: 
            print('Empresa cadastrada com sucesso!')
            fim = True

            
    
