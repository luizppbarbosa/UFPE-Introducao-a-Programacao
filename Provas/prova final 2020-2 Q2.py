
def procedimento (num):
    if num % 7 == 0 and num % 5 == 0:
        print(f'O número {num} é multiplo de 7 e de 5 ')
    if num % 7 == 0 and num % 11 != 0:
        print(f'O número {num} é múltimo de 7 mas não é de 11 ')
    




num = int(input('Digite o primeiro número: '))
cont = 0

while num != 0 and cont <= 100:
    if num % 7 != 0:
        print('O número digitado não é multiplo de 7 ')
    else:
        cont += 1
        print('O número digitado é múltimo de 7 ')
        procedimento(num)
    num = int(input('Digite o próximo número: '))

