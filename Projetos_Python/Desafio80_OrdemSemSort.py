lista = []

for c in range(0, 5):
    adicionar = int(input('Digite um valor a ser adicionado na lista: '))
    if not lista:
        lista.append(adicionar)
    else:
        adicionado = False #criando variável de controle 
        
        for posicao, valor in enumerate(lista):
            if adicionar <= valor:
                lista.insert(posicao, adicionar)
                adicionado = True
                break
    
        if not adicionado:
                lista.append(adicionar)

print(lista)