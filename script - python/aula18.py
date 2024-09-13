teste = []
teste.append('Gustavo')
teste.append(40)
print(teste)

galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0])
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

pessoal = []
dado = []
totalMaior = totalMenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoal.append(dado[:])
    dado.clear()
print(pessoal)
for p in pessoal:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        totalMaior+=1
    else:
        print(f'{p[0]} é menor de idade!')
        totalMenor+=1
print(f'Temos {totalMaior} maiores de idade e {totalMenor} menores de idade')