from math import sqrt
import random

num = int(input('Digite um numero: '))
raiz = sqrt(num)
print(f'A raiz de {num} é de {raiz:.2f}')

print(f'Gerando um numero aleatório: ')
num = random.randint(1, 10)
print(num)
