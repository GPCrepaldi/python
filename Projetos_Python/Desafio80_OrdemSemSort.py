lista = []

for c in range(0, 5):
    adicionar = int(input('Digite um valor a ser adicionado na lista: '))

    if not lista or adicionar > lista[-1]: #condição para caso a lista esteja vazia, ou o valor digitado seja maior do que o ultimo valor
        lista.append(adicionar)
        print(f'valor adicionado no final da lista!')
    else:
        for posicao, valor in enumerate(lista): #laço que verificará todos os valores dentro da lista
            if adicionar <= valor: #caso o numero digitado seja menor ou igual ao valor que esta na posição analizada, ele será posto no lugar
                lista.insert(posicao, adicionar)
                print(f'Valor adicionado na posição {posicao}!')
                break

print(lista)