def mediapond(nome, peso1 = 1, peso2 = 1):
    
    nota1 = float(input(f'Digite a primeira nota do aluno {nome}: '))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input(f'ERRO. Digite uma nota válida: '))

    nota2 = float(input(f'Digite a segunda nota do aluno {nome}: '))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input(f'ERRO. Digite uma nota válida: '))

    media = ((nota1 * peso1) + (nota2 * peso2)) / (peso1 + peso2)

    if media >= 7:
        sit = 'está aprovado'
    elif media < 3:
        sit = 'está reprovado'
    else:
        sit = 'fará prova final'

    print(f'O aluno {nome} obteve a média {media} e {sit}')

nome = input('Digite o nome do aluno: ')
peso1 = float(input('Digite o valor do peso da primeira nota: '))
peso2 = float(input('Digite o valor do peso da segunda nota: '))

mediapond(nome, peso1, peso2)