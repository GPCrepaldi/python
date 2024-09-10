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

if tupla.count(3) != 0: #Criado para verificar se tem o 3 na tupla ou n, pq se n tiver, da erro
    print(f'O numero 3 está na posição: {tupla.index(3)+1}') #coloquei o +1 para ficar melhor visível a posição do numero
    print('-=' * 30)
else:
    print('Não há numero 3 na tupla!!')
    print('-=' * 30)

print(f'Os numero pares foram:', [num for num in tupla if num % 2 == 0]) #eu fiz o If dentro do print, para diminuir as linhas