maioresIdades = homens = mulheresMenores = 0

while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Digite seu sexo (M / F): ')).strip().lower()[0]

    if idade > 17:
        maioresIdades += 1
    if sexo == 'm':
        homens += 1
    if idade < 20 and sexo == 'f':
        mulheresMenores += 1

    escolha = ' '
    while escolha not in 'ns':
        escolha = str(input('Você quer continuar? (S / N): ')).strip().lower()[0]
    if escolha == 'n':
        break

print(f'tem {maioresIdades} Maiores de Idade')
print(f'Tem {homens} homens')
print(f'Tem {mulheresMenores} mulheres com menos de 20 anos')