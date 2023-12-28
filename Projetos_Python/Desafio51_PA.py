inicio = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

for repetir in range(1, 11):
    print(inicio, end=' ► ')
    inicio += razao
print('FIM')


#   O jeito do Guanabara fazer:

#   decimo = inicio + (10 - 1) * razao
#   for repetir in range(inicio, decimo, razao):
#       print(repetir, end=' ► ')
#   print('ACABOU')
