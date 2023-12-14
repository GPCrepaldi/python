produto = float(input('Digite o valor do produto: '))
print('[ 1 ] A vista')
print('[ 2 ] Cartão')
print('[ 3 ] Parcelamento em até 2x')
print('[ 4 ] Parcelamento de 3x ou mais')
pagamento = int(input())

if pagamento == 1:
    resultado = produto * 0.9
elif pagamento == 2:
    resultado = produto * 0.95
elif pagamento == 3:
    resultado = produto
    divisao = produto / 2
    print(f'Seu produto será parcelado em 2x de R${divisao}')
elif pagamento == 4:
    resultado = produto * 1.2
    parcelas = int(input('Em quantas parcelas irá pagar? '))
    divisao = produto / parcelas
    print(f'Sua compra será parcelado em {parcelas} vezes de R${divisao:.2f}')
else:
    resultado = "forma de pagamento inválida"

print(f'Sua compra deu R${produto}, Seus produtos estão saindo por.... R${resultado:.2f}')
print('')
