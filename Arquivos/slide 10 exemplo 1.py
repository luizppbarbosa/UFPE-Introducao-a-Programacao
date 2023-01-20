def separanum(a):

    lista1 = []


    for i in range (5):
        lista1.insert(0,a%10)
        a = a // 10
    
    return (lista1)

def contnum(num,dig):

    lista = separanum(num)
    print(lista)

    if dig in lista:
        print(f'O dígito {dig} ocorre em {num} {lista.count(dig)} vezes')
    else:
        print(f'O dígito {dig} não aparece em {num}')




num = int(input('Digite um número inteiro positivo de 5 dígitos: '))
while num <= 0 or num > 99999:
    num = int(input('ERRO. Digite um número inteiro positivo de até 5 dígitos: '))


while num > 0:

    dig = int(input(f'Qual dígito de 0 a 9 você quer procurar em {num} ? '))
    while dig < 0 or dig > 9:
        dig = int(input('ERRO. Digite apenas um dígito positivo: '))

    contnum(num,dig)
    num = int(input('Digite o próximo número inteiro positivo de 5 dígitos ( <= 0 para ): '))
    while num > 99999:
        num = int(input('ERRO. Digite o próximo número com no máximo 5 dígitos ( <= 0 para ) : '))




print('Condição de parada digitada. Fim do programa')
