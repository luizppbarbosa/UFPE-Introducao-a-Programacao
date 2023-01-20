M = int(input('Digite a quantidade de linhas da matriz (<=4): '))
N = int(input('Digite a quantidade de colunas da matriz (<=8): '))

mat = []
mult6 = []

for i in range (M):
    mat.append([0]*N)

print(mat)

for i in range (M):
    for j in range (N):
        mat[i][j] = int(input(f'Digite o elemento da {i+1} linha {j+1} coluna: '))
    
print(mat)

for j in range (N):
    for i in range (M):
        if mat[i][j] % 6 == 0:
            mult6.append(mat[i][j])

for i in range (M):
    print (mat[i])

print(mult6)