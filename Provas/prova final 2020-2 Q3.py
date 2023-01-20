leitura = open('clientes.txt','r')

pontosmin = int(input('Digite o valor mínimo de pontos'))
while pontosmin <= 1000:
    pontosmin = int(input('ERRO. O valor mínimo de pontos deve ser maior que 1000'))

cont1 = 0
cont2 = 0
soma = 0

with leitura:
    for linha in leitura:
        matricula = linha [0:4]
        nome = linha [5:35]
        sexo = linha [36:37]
        pontos = int(linha[38:43])
        cont1 += 1

        if int(pontos) > pontosmin:
            print(f'{matricula} {pontos}')
            cont2 += 1
            soma += pontos

media = soma / cont2

print(f'Foram lidos {cont1} registros! ')
print(f'Foram impressos {cont2} clientes! ')
print(f'A média das pontuações dos clientes impressos é igual a {media}')