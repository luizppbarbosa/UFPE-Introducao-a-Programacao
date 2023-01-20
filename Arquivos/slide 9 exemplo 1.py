
curso = {}

print('Vamos iniciar o preenchimento da tabela. \n')

cod = int(input('Digite o código do curso: '))
while cod <= 0:
    cod = int(input('Digite pelo menos um código válido de curso! '))

while cod > 0:
    nome = str(input('Digite o nome do curso: '))
    centro = int(input('Digite o número do centro: '))
    curso[cod] = (nome,centro)
    cod = int(input('Digite o próximo código de curso: '))

print(curso[0][1])

"""print('Vamos iniciar a consulta da tabela por código de centro: \n')

codcen = int(input('Digite o código de centro para ver os cursos associados a ele: '))
while codcen > 0:
    if codcen in curso:"""
         