n = int(input('Digite o numero da tabuada: '))

multiplicador = 0

for multiplicador in range (0, 11):
    print(f'{n} * {multiplicador} = {n*multiplicador}')