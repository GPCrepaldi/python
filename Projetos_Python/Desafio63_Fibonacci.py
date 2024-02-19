n = int(input('Digite um numero: '))
cont = 2
primeiro = 0
proximo = 1

print(f'{primeiro} » {proximo} » ', end='')

while cont < n:
    sequencia = primeiro + proximo
    print(f'{sequencia}', end=' » ')
    primeiro = proximo
    proximo = sequencia
    cont += 1

print('FIM')
