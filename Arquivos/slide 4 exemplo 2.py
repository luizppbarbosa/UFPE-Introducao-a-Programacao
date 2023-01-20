num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

while num2 == 0:
    num2 = int(input('ERRO, o segundo número não pode ser ZERO. Digite o segundo número: '))

resto = num1%num2

if resto == 0:
    print(f'O resto da divisão foi zero, {num1}')
else:
    print(f'O resto da divisão não foi zero, {resto**2}')