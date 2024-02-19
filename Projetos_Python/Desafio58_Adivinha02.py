from random import randint
from time import sleep

computador = randint(0, 10)
tentativas = 1

jogador = int(input('Digite o numero que acha que o computador escolheu: '))

while jogador != computador:
    sleep(0.5)
    if computador < jogador:
        jogador = int(input('Menos... Você errou, tente novamente: '))
        tentativas += 1
    elif computador > jogador:
        jogador = int(input('Mais... Você errou, tente novamente: '))
        tentativas += 1
sleep(0.5)
print(f'Parabêns, você acertou!!!! o numero escolhido foi {computador}, você tentou {tentativas} vezes')