txt1 = input('Digite o primeiro texto: ')
txt2 = input('Digite o segundo texto: ')
cont = 0
pos = 0
tam = len(txt1)
incr = 0


while pos != -1:
    pos = txt2.find(txt1,incr)
    incr = pos + tam 
    if pos != -1:
        cont += 1
    
print(f'\'{txt1}\' aparece em \'{txt2}\' um total de {cont} vezes')