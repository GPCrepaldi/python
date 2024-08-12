lanche = ('Hambuguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#Tuplas são imutáveis

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('-=' * 30)

for comida in lanche:
    print(f'E vou comer {comida}')

print('-=' * 30)

for pos, comida in enumerate(lanche):
    print(f'E vou comer {comida} na posição (pos)')

print('-=' * 30)

print('Comi para caramba')

print(sorted(lanche))
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(c.count(5))
print(c.index(5))

pessoa = ('Gustavo', 39, 'M', 99.88)
#del(pessoa) #você só pode deletar a tupla completamente, e não só uma caracteristica dentro dela
print(pessoa)