from datetime import date

ano = int(input('Digite o ano que você nasceu: '))
data = date.today().year

idade = data - ano
falta = 18 - idade
passou = idade - 18

if idade < 18:
    print(f'Você tem {idade} anos ainda não tem que se alistar! falta {falta} anos para você se alistar')
    print(f'Seu alistamento vai ser em {ano + 18}')
elif idade == 18:
    print(f'Você está com {idade} anos, na idade de se alistar no exercito!!!!... su fudeu')
else:
    print(f'Você ja tem {idade} anos, passou {passou} anos de seus alistamento')
    print(f'Seu alistamento foi em {ano + 18}')
