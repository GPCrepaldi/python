gasto = custaCaro = 0
maisBarato = None

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: '))

    gasto += preco

    if preco > 1000:
        custaCaro += 1

    if maisBarato is None or preco < maisBarato:
        nomeMaisBarato = nome
        maisBarato = preco

    escolha = ' '
    while escolha is not 'sn':
        escolha = str(input('Você quer continuar?(S / N)')).strip().lower()[0]
    if escolha == 'n':
        break

print(f'O total gasto foi de R${gasto:.2f} reais')
print(f'Teve {custaCaro} produtos acima de R$1.000,00 reais')
print(f'E o produto mais barato foi {nomeMaisBarato} custando R${maisBarato:.2f}')
