from datetime import date

ano = int(input('Digite o ano que você nasceu: '))
data = date.today().year
idade = data - ano

print(f'O atleta tem {idade} anos!')

if idade <= 9:
    print(f'MIRIM')
elif idade <= 14:
    print(f'INFANTIL')
elif idade <= 19:
    print(f'JUNIOR')
elif idade <= 25:
    print(f'SÊNIOR')
else:
    print(f'MASTER')
