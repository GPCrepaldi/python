produtos = (
    'Arroz', 40,
    'Feijão', 25,
    'Macarrão', 17.5,
    'Molho de Toamte', 4.99,
    'Detergente', 7.99,
    'Desinfetante', 23.99,
    'Pasta de Dente', 4.50,
    'Escova de dente', 3.99
)

print('-' * 40)
print('PREÇOS DO MERCADO'.center(40))
print('-' * 40)
for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f'{nome:.<30} R$ {preco:>5.2f}')
print('-' * 40)

print('OUTRO METODO') #o primeiro metodo, foi eu fazendo sozinho, ja o segundo é a correção do exercicio

print('-' * 40)
print(f'{'PREÇOS DO MERCADO':^40}')
print('-' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-'*40)