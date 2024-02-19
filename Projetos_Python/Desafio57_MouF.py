sexo = str(input('Digite o seu sexo (M/F): ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Você digitou errado, tente novamente (M/F): ')).strip().upper()[0]

print(f'O seu sexo é: {sexo}')