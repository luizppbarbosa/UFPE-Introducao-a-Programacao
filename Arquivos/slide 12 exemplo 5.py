
leitura = open('titanic.txt', 'r')
escrita = open('sobreviventes.txt', 'w')
conth = 0
contm = 0
idade = 0

with leitura, escrita:
    for linha in leitura:
        lista = linha.split(',')
        if lista[1] == '1':
            escrita.write(f'{lista[3]}, {lista[4]}, {lista[5]}\n')
            if lista[4] == 'male':
                conth += 1
                idade += float(lista[5])
            else:
                contm += 1
                idade += float(lista[5])

med = idade / (conth + contm)

print(f'{conth} sobreviventes homens')
print(f'{contm} sobreviventes mulheres')
print(f'A média da idade de todos os sobreviventes é: {med:.2f}')

