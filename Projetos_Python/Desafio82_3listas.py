lista = []
listaPar = []
listaImp = []
resp = 'S'

while resp == 'S':
    lista.append(int(input('Digite o valor a ser adicionado na lista: ')))

    resp = str(input('Você deseja continuar? [S/N]: ')).upper()
    while resp != 'S' and resp != 'N':
        resp = str(input('Digite a resposta corretamente! [S/N]: ')).upper()

for indice, valor in enumerate(lista):
    if valor % 2 == 0:
        listaPar.append(valor)
    else:
        listaImp.append(valor)

print('-=' * 30)
print(lista)

print('-=' * 30)
print(listaPar)

print('-=' * 30)
print(listaImp)