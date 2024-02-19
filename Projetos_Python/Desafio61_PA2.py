primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão que a PA vai seguir: '))
contador = 0

while contador < 10:
    print(f'{primeiro}', end=' ► ')
    primeiro += razao
    contador += 1

print('FIM')