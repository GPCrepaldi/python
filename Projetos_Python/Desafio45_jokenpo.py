import random
import time

computador = ['pedra', 'papel', 'tesoura']

print('Vamos jogar Jokenpô... Vamos ver se consegue ganhar de mim....')

print('[ 1 ] Pedra')
print('[ 2 ] papel')
print('[ 3 ] tesoura')
jogador = int(input())

escolhendo = random.choice(computador)

if jogador == 1:
    print('Você escolhei PEDRA')
    time.sleep(1)
    if escolhendo == 'pedra':
        print('EMPATAMOS!!! eu também escolhi PEDRA...')
    elif escolhendo == 'papel':
        print('PERDEU!!! eu escolhi PAPEL...')
    else:
        print('GANHOU!!! eu escoli TESOURA...')
elif jogador == 2:
    print('Você escolheu PAPEL')
    time.sleep(1)
    if escolhendo == 'pedra':
        print('GANHOU!!! eu escolhi PEDRA...')
    elif escolhendo == 'papel':
        print('EMPATAMOS!!! eu também escolhi PAPEL...')
    else:
        print('PERSEU!!! eu escoli TESOURA...')
elif jogador == 3:
    print('Você escolheu TESOURA')
    time.sleep(1)
    if escolhendo == 'pedra':
        print('PERSEU!!! eu escolhi PEDRA...')
    elif escolhendo == 'papel':
        print('GANHOU!!! eu escolhi PAPEL...')
    else:
        print('EMPATAMOS!!! eu também escoli TESOURA...')
else:
    print('Escolha inválida.....')

print('')
