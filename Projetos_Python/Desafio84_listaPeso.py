dados = []
pessoas = []
contador = 0

#laço para adicionar os dados da primeira lista na segunda
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:]) #adicionando os dados na segunda lista
    dados.clear() #limpando a primeira lista
    contador += 1
    
    resposta = str(input('Quer continuar? [S/N]: ')).upper()
    if resposta == 'N':
        break

for p in pessoas:
    print('n sei fazer essa bomba aqui n')

print('-=' * 30)
