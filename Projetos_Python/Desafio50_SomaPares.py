soma = 0
cont = 0
print('Só somaremos números pares....')

for intervalo in range(1, 7):
    numero = int(input('Digite o numero que você quer somar: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print(f'Você me informou {cont} numeros pares e o valor da soma é de: {soma}')