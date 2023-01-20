#Cálcular o valor da soma da série S

num = 3 
den = 2
div = 1

for i in range (2,51):
    div = (num / den) + div
    num += 2
    den += 1
    
print(f'A soma da série é igual a {div}')