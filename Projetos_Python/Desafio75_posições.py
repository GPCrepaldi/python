tupla = (
    int(input('Digite um valor a ser adicionado na Tupla: ')),
    int(input('Digite um valor a ser adicionado na Tupla: ')),
    int(input('Digite um valor a ser adicionado na Tupla: ')),
    int(input('Digite um valor a ser adicionado na Tupla: '))
)
print('-=' * 30)

print(tupla)
print('-=' * 30)

print(f'O numero 9 aparece: {tupla.count(9)} vezes')
print('-=' * 30)

if tupla.count(3) != 0:
    print(f'O numero 3 está na posição: {tupla.index(3)}')
    print('-=' * 30)
else:
    print('Não há numero 3 na tupla!!')
    print('-=' * 30)

print(f'Os numero pares foram:', [num for num in tupla if num % 2 == 0])