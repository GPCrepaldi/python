lista = []
resp = 'S'

while resp == 'S':
    lista.append(int(input('Digite o valor que deseja cadicionar na Lista: ')))

    resp = str(input('Você deseja continuar?[S/N]: ')).upper()
    while resp != 'S' and resp != 'N':
        resp = str(input('Digite a resposta corretamente! [S/N]: ')).upper()

print('-=' * 30)
print(f'Foram digitador {len(lista)} elementos:')
print(lista)

print('-=' * 30)
print(f'A lista ordenada de forma decrescente fica:')
lista.sort(reverse=True)
print(lista)

print('-=' * 30)
if 5 in lista:
    print(f'O numero 5 foi digitado na lista!')
else:
    print(f'O numero 5 não foi digitado na lista')