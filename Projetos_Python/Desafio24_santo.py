cidade = str(input('Digite o nome da sua cidade: ')).strip()

reformulando = cidade.title()
if reformulando.startswith('Santo'):
    print(f'Há a palavra Santo no começo')
else:
    print(f'Não há a palavra santo no começo')

# segunda forma de resolver

print(cidade[:5].title() == 'Santo')
