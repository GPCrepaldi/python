from datetime import date

ano = int(input('Digite o ano que quer saber (use 0 para o ano atual): '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissesto!!')
else:
    print(f'O ano {ano} não é bissesto!!')