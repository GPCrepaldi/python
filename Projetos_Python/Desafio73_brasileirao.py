brasileirao = ('Athlético - PR', 'Bahia', 'Flamengo', 'Botafogo', 'São Paulo', 'Cruzeiro', 'Atlético - MG', 'Bragantino', 'Palmeiras', 'Internacional', 'Fortaleza', 'Grêmio', 'Vasco da Gama', 'Crciúma', 'Juventude', 'Corinthians', 'Fluminense', 'EC Vitória', 'Atlético - GO', 'Cuiabá')

print(f'-=' * 40)
print(f'Aqui os 5 primeiros colocados do Brasileirão de 2024: \n{brasileirao[0:6]}')

print(f'-=' * 40)
print(f'Os ultimos 4 colocados do Brasileirão 2024: \n{brasileirao[-4:]}')

print(f'-=' * 40)
print(f'O times do Brasileirão 2024 ordenados de forma alfabética: \n{sorted(brasileirao)}')

print(f'-=' * 40)
print(f'Em qual posição da tabela está o Flamengo: \nO Flamengo está na {brasileirao.index('Flamengo')+1}ª posição')

print(f'-=' * 40)