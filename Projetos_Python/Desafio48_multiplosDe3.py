print('Aqui você verá a soma dos multiplos de 3 entre 1 e 500...')
soma = 0
contador = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        soma += numero
        contador += 1

print(f'A soma dos {contador} numeros é de {soma}')
