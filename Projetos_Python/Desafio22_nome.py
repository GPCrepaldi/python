nome = str(input('Digite o seu nome: ')).strip()

print('Analisando o seu nome....')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')

print('Seu nome tem ao todo {} letras'.format(
    len(nome) - nome.count(' ')))  # forma 1
print(f'Seu nome tem ao todo {len(nome.replace(" ", ""))} letras')  # forma 2

separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')  # forma 1
print('Seu primeiro tem {} letras'.format(nome.find(' ')))  # forma 2
