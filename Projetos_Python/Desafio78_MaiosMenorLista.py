numeros = []

for n in range(0, 5):
    numeros.append(int(input(f'Digite o valor a ser adicionado na posição {n}: ')))
print(numeros)

print(f'\nO maior valor foi {max(numeros)} na posição(ões): ', end='')
for i, valor in enumerate(numeros): #neste caso eu n pude usar o index, pq o index apenas retorno a primeira ocorrencia do valor
    if valor == max(numeros):
        print(f'{i} ', end='')

print(f'\nO menor valor foi {min(numeros)} na posição(ões): ', end='')
for i, valor in enumerate(numeros): #sendo assim, é melhor usar o enumerate, pq ele vai numerando todo vetor(lista)
    if valor == min(numeros):
        print(f'{i} ', end='')