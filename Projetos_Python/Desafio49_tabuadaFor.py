tabuada = int(input('A tabuada de qual numero você quer ver? '))

print('=-'*20)
for multiplicador in range(0, 11):
    print(f'{tabuada} * {multiplicador} = {tabuada * multiplicador}')
print('=-'*20)