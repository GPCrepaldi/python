pessoas = ['Gabriel', 'Socorro', 'Diego', 'Emily', 'Andressa']

maior = 0
menor = 0

for i in pessoas:
    peso = float(input(f'{i}, Digite o seu peso: '))
    if peso > maior:
        maior = peso
    elif peso < maior and menor == 0:
        menor = peso
    elif peso < menor:
        menor = peso

print(f'O maior peso lido foi de {maior} e o menor peso lido foi de {menor}')
