r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Estas retas podem formar um triangulo!!!')
    if r1 == r2 == r3:
        print(f'Este triangulo é Equilátero!!')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print(f'Este triangulo é Isóceles')
    else:
        print(f'Este triangulo é Escaleno')
else:
    print('Estas retas não podem formar um triangulo...')
