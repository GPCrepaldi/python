primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão que a PA vai seguir: '))
termos = int(input('Quantos termos você qquer ver? '))
contador = 0

while termos != 0:
    if contador < termos:
        print(f'{primeiro}', end=' ► ')
        primeiro += razao
        contador += 1
    elif contador == termos:
        termos = int(input('\nVocê deseja ver mais quantos termos: '))
        contador = 0

print('FIM')