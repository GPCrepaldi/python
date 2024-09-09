lanche = ('Hambuguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#Tuplas são imutáveis

print('Exemplo 1')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
#este for da o mesmo resultado do que o For a seguir (exemplo 2)

print('-=' * 30)

print('Exemplo 2')
for comida in lanche:
    print(f'E vou comer {comida}')
print(f'Comi para Caramba!!')
#Este for da o mesmo resultado que o for anterior (exemplo 1)

print('-=' * 30)

print('Exemplo 3')
for pos, comida in enumerate(lanche):
    print(f'E vou comer {comida} na posição {pos}')
#Este for tem a mesma execução que o proximo for (exemplo 4)

print('-=' * 30)

print('Exemplo 4')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
#Este for tem a mesma execução que o for anterior (exemplo 3)

print('-=' * 30)

print('Exemplo 5')
print(sorted(lanche))
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(c)
print(len(c))
print(c.count(5))
print(c.index(5))
print(c.index(5,1))

print('-=' * 30)

print('Exemplo 6')
pessoa = ('Gustavo', 39, 'M', 99.88) #pode criar tuplas com tipos de dados diferentes, como neste exemplo que tem numeros e strings
#As tuplas podem ser apagas com o comando del(pessoal) por exemplo
print(pessoa)