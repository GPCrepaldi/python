expressao = str(input('Digite a expressão matemática: ')).strip()
contador = 0

for indice, valor in enumerate(expressao):
    if valor == '(':
        contador+=1
    elif valor == ')':
        contador-=1

if contador == 0:
    print('A expressão etá correta!!')
else:
    print('A expressão está incorreta!!')