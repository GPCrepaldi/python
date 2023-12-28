from datetime import date

ano = date.today().year

pessoas = ['Perseu', 'Jotas', 'Diego', 'Nathalia', 'Ednei', 'Gabriel', 'Julia']

maior = 0
menor = 0

for i in pessoas:
    nascimento = int(input(f'{i}, Digite seu ano de nascimento: '))
    maioridade = ano - nascimento
    if maioridade < 21:
        print(f'{i} ainda não atingiu a maioridade de 18 anos, tendo apenas {maioridade} anos')
        maior += 1
    else:
        print(f'{i} já atingiu a maioridade de 18 anos, tendo {maioridade} anos')
        menor += 1

print('=-'*20)
print(f'No total, tem {maior} pessoas que ja atingiram a maioridade e {menor} que ainda não atingiram a maioridade')
print('=-'*20)
