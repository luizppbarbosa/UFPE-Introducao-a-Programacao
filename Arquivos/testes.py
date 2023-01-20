
num = 12345


algarismos = [-1] * 5
pos = 0
while num != 0:
        algarismos[pos] = num % 10
        num //= 10
        pos += 1


print(algarismos)