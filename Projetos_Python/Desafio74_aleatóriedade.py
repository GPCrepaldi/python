from random import randint

aletório = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print(aletório)

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