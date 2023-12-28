num = int(input('Digite um numero para ver se ele é primo: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[32m', end=' ')
        total += 1
    else:
        print(f'\033[31m', end=' ')
    print(f'{c} \033[0m', end=' ')

print(f'O numero {num} foi dividido {total} vezes!')

if total == 2 and num > 2:
    print(f'O numero {num} é um número primo!')
else:
    print(f'O numero {num} não é um número primo....')