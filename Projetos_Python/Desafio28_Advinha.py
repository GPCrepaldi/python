from random import randint
from time import sleep

computador = randint(0, 5)

print('-=-=' * 20)
print('Estou pensando em um numero de 0 a 5... Tente adivinhar!!!')
print('-=-=' * 20)
jogador = int(input('Digite o valor que acha que o computador escolheu de 0 a 5: '))

print('PROCESSANDO....')
sleep(1)

if jogador == computador:
    print(f'Parabens você acertou, eu pensei em {computador}')
else:
    print(f'Você errou, eu pensei em {computador} e não em {jogador}')
