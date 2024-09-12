lista = []
resp = 'S'

while resp == 'S':
    #receber um valor para averiguar se será adicionado a lista ou n
    adicionar = int(input('Qual o valor que vc deseja adicionar a lista?: '))
    
    #checagem para averiguar se o valor digitado ja está na lista, caso esteja, ele n será adicionado
    if adicionar in lista: #com o comando 'in' eu posso averiguar diretamenta algo que está 'dentro' de outra coisa
        print('Sinto muito, esse valor ja foi adicionado')
    else:
        lista.append(adicionar)
        print('Numero adicionado com sucesso!!')
    
    #pergunto para ver se o usuário irá continuar
    resp = str(input('Você deseja continuar? [S/N]')).upper()
    
    #verificarção da resposta do usuário
    while resp != 'S' and resp != 'N':
        resp = str(input('Digite a resposta corretamente seu burro!!! [S/N]')).upper()
        if resp == 'N':
            break

print('-=' * 40)

#ordena e printa na tela
lista.sort()
print(lista)