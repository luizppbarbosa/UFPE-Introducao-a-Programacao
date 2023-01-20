
def separanum(n):
    
    lista =[-1]*4
    pos = 0

    while n != 0:
        lista[pos] = n % 10
        n = n // 10
        pos += 1
   
    return lista

def palindromo (num):
    lista2 = separanum (num)
    n = 0
    pos = 0
    while pos < 4 and lista2[pos] != -1:
        n = n * 10 + lista2[pos]
        pos += 1
    return n




for i in range (100,5001):
    palindromo(i)
    if i == palindromo(i):
        print(i)

        
