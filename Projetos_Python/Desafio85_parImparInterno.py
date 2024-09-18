numeros = []
par = []
impar = []

for c in range(0, 7):
    adiciona = int(input(f'Digite o {c+1}º numero: '))
    if adiciona % 2 == 0:
        par.append(adiciona)
    else:
        impar.append(adiciona)
        
numeros.append(par[:])
numeros.append(impar[:])
par.clear()
impar.clear()

print(f'Os numeros pares são: {numeros[0]}')
print(f'Os numeros impares são: {numeros[1]}')