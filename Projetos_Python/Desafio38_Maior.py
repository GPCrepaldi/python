n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print(f'o numero {n1} é maior que {n2}')
elif n2 > n1:
    print(f'o numero {n2} é maior que {n1}')
else:
    print(f'o numero {n1} e {n2} são iguais')
