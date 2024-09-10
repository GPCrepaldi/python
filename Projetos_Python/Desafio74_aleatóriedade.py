from random import randint

aletório = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print('-=' * 10)

print(aletório)

print('-=' * 10)

oMaior = ' '
for maior in aletório:
    oMaior = aletório[0]
    
    if aletório[1] > oMaior:
        oMaior = aletório[1]
    elif aletório[2] > oMaior:
        oMaior = aletório[2]
    elif aletório[3] > oMaior:
        oMaior = aletório[3]

print(f'O Maior valor é {oMaior}')
print(f'O Maior valor é {max(aletório)}') #isso faz a mesma função que o if super gigante que eu fiz anteriormente

print('-=' * 10)

oMenor = ' '
for menor in aletório:
    oMenor = aletório[0]

    if aletório[1] < oMenor:
        oMenor = aletório[1]
    if aletório[2] < oMenor:
        oMenor = aletório[2]
    if aletório[3] < oMenor:
        oMenor = aletório[3]

print(f'O Menor valor é {oMenor}')
print(f'O Menor valor é {min(aletório)}')#isso faz a mesma coisa que o max, só que com o valor minimo