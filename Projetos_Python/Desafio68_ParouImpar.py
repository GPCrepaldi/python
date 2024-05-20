import random

num = maquina = contador = 0

while True:
    escolha = str(input('Você quer PAR ou IMPAR? ')).strip().lower()
    num = int(input('Digite um número: '))
    maquina = random.randint(0, 10)
    decisao = maquina + num
    if decisao % 2 == 0 and escolha == 'par':
        print(f'Parabéns, você escolheu {num} e eu {maquina} dando {decisao}! Você venceu!!!!')
        contador += 1
    elif decisao % 2 != 0 and escolha == 'impar':
        print(f'Parabéns, você escolheu {num} e eu {maquina} dando {decisao}! Você venceu!!!!')
        contador += 1
    else:
        print(f'Infelizmente, deu {decisao}! Você perdeu!!!!')
        break
print(f'Você conseguiu {contador} vitórias seguidas...')
