with open ('meupiru.txt','r') as escrita:
    for linha in escrita:
        a, b = linha.split()
        print (f'{b} meu piru {a}')
