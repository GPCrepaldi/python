distancia = int(input('Digite a distacia da sua viagem: '))

if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45

print(f'O valor da sua viagem ficará R${valor:.2f} !!!')

valor = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print(f'O valor da sua viagem ficará R${valor:.2f} !!!')
