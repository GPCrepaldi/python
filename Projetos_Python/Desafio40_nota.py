n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))

media = (n1 + n2 + n3) / 3

if media < 5:
    print(f'Infelizmente você foi reprovado com média de {media:.2f}')
elif media < 7:
    print(f'Você está de recuperação devido a sua media anual estar {media:.2f}')
else:
    print(f'PARABÉNS!!!! Você passou de ano com média de {media:.2f}')
    