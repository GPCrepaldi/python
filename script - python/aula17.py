print('-=' * 40, 'Exemplo 1')
num = [2, 5, 9, 11] #criação de uma lista
print(num)
num[2] = 3 #trocando os valores na posição desejada
print(num)
num.append(2) #adicionando conteúdo na lista pelo final
print(num)
num.sort() #ordena a lista de forma crescente
print(num)
num.sort(reverse=True) #ordena a lista de forma decrescente
print(num)
num.insert(2, 0) #insere na posição '2' o valor '0', fazendo com que os valores seguintes se desloquem para a proxima casa
print(num)
num.pop(2) #deleta a posição '2'
print(num)
num.remove(2) #deleta o primeiro conteudo desejado que será encontrado na lista, neste caso, o primeiro '2' (deve ser usado o conteudo e não a posição em que ele se encontra na lista)
print(num)
if 5 in num: #criando condições de exclusão
    num.remove(5)
else:
    print('não achei o numero 5')
print(num)
print(f'Essa lista tem {len(num)} elementos')

print('-=' * 40, 'Exemplo 2')

valores = []
valores.append(1)
valores.append(3)
valores.append(9)

for c, v in enumerate(valores): #forma de ler toda a lista dinamicamente
    print(f'Na posição {c}, encontrei o valor {v}')
print('Cheguei ao final da lista')

print('-=' * 40, 'Exemplo 3')

numeros = []
for cont in range(0, 5): #adicionar valores na lista de forma interatica com o usuario
    numeros.append(int(input('Digite o valor a ser adicionado: ')))
print(numeros)

print('-=' * 40, 'Exemplo 4')

a = [2, 3, 4, 7]
b = a #desta forma, ao inves de vc simplesmente criar uma cópia da lista, vc esta vinculando as duas listas
print(f'Lista A: {a}')
print(f'Lista B: {b}')
c = a[:] #esta é a forma correta de se criar uma cópia da outra lista
c[2] = 8
print('Após a troca')
print(f'Lista A: {a}')
print(f'Lista C: {c}')
b[2] = 8 #sendo assim... como a lista A e B estão vinculadas, ao alterar uma, eu mudo a outro automaticamente
print('Após a troca')
print(f'Lista A: {a}')
print(f'Lista B: {b}')