#TIPO FUNÇÃO!!


def MultiplicaDigitos(num):
    mult = 1

    if num <= 0:
        mult = -1

    elif num > 999999:
        mult = -2
    
    else:
        lista =[-1]*6
        pos = 0

        while num != 0:
            lista[pos] = num % 10
            num = num // 10
            pos += 1

        for i in lista:
            if i != 0 and i != -1:
                mult *= i

    
    return mult


num = int(input('Digite num! '))

mult = MultiplicaDigitos(num)

print(mult)