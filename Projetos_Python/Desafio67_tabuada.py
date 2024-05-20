num = tabuada = 0

while True:
    num = int(input('Digite a tabuada que quer ver: '))
    
    print('-' * 20)
    if num < 0:
        break
    for i in range(0, 11, 1):
        tabuada = num * i
        print(f'{num} X {i} = {tabuada}')
    print('-' * 20)

print('Você está saindo do sistema')