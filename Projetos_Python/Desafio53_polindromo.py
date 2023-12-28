frase = str(input('Digite a sua frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)

print(f'Você digitou: {junto} que fica: {junto[::-1]}')

if junto == junto[::-1]:
    print('A frase é um Palindrómo!')
else:
    print('A frase não é um Palindrómo')
