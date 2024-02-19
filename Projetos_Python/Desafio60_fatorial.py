from math import factorial

fatorar = int(input('Digite um numero que deseja fatorar: '))
resultado = 1

print('============= Metodo 1')
f = factorial(fatorar)
print(f'O fatorial de {fatorar}! é {f}')

print('============= Metodo 2')
print(f'O fatorial de {fatorar}! = ', end='')
while fatorar > 0:
    print(f'{fatorar}', end='')
    print(' x ' if fatorar > 1 else ' = ', end='')
    resultado *= fatorar
    fatorar -= 1

print(f'{resultado}\n')
