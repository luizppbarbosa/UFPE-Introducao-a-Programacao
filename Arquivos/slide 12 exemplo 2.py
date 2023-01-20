

def leitura():
    tab = {}
    with open('profissoes.txt','r') as arq:  #arquivo não existir
        for linha in arq:
            cod, prof = linha.split('\t')
            tab[int(cod)] = prof
    
    return tab

fim = False
while not fim:
    try:
        tabela = leitura()
        
        cod = int(input('Digite um código para pesquisar a profissão: '))  #digitar valor do tipo errado
        while cod <= 0:
            cod = int(input('ERRO. Digite pelo menos um código válido: '))

        while cod > 0:
            if cod in tabela:
                print(f'A profissão referente ao código {cod} é {tabela[cod]}')
            else:
                with open('profissoesinexistentes.txt', 'a') as escrita:
                    escrita.write(f'{cod}\n')  #problema de acesso ao diretório
                print('Profissão Inexistente')

            cod = int(input('Digite o próximo código para pesquisar a profissão: '))

        

    except ValueError:
        print('ERRO, valor inconsistente digitado! ')

    except PermissionError:
        print('Usuário sem acesso ao local de escrita! ')
        fim = True

    except FileNotFoundError:
        print('Arquivo inexistente! ')
        fim = True

    else:
        print ('Código inválido digitado. Fim do programa! ')
        fim = True