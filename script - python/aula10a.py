nome = str(input('Qual o seu nome: ')).strip()

if nome == 'Gustavo':
    print('Que nome lindo você tem!!')
else:
    print('Seu nome é tão normal, Bom dia!!!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

if m <= 5:
    print('Estude mais')
else:
    print('Parabens, suas notas são boas')
