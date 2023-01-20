N = int(input('Digite a quantidade de alunos: '))
while N < 1:
    N = int(input('ERRO. Digite uma quantidade de alunos maior que zero: '))

notas = [0]*N
notasm = [0]*N
cont = 1
contm = 0
soma = 0

for i in range (N):
    notas[i] = float(input(f'Digite a nota do {cont}º aluno: '))
    soma += notas[i]
    cont += 1

media = soma/N

for i in range (N):
    if notas[i] >= media:
        notasm[contm] = notas[i]
        contm += 1

notasm = notasm [:contm]
print (f'As notas da turma foram: \n {notas}')
print (f'A média da turma foi {media}')
print (f'As notas acima da média turma foram: \n {notasm}')