from math import floor, trunc

num = float(input('Digite um numero: '))
print(f'O numero {num} tem parte inteira {floor(num)}')  # usando floor
print(f'O numero {num} tem parte inteira {trunc(num)}')  # usando trunc
print(f'O numero {num} tem parte inteira {int(num)}')  # usando int
