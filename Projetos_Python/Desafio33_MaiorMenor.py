n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n3:
    maior = n2
else:
    maior = n3

print(f'O maior numero é {maior}')

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n3:
    menor = n2
else:
    menor = n3

print(f'O menor numero é {menor}')
