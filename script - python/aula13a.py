for c in range(0, 7, 2):
    print(c)
print('Fim')

print(' ')

for i in range(7, 0, -1):
    print(i)
print('Fim')

print('')

n = int(input('Digite um valor: '))
for j in range(0, n+1):
    print(j)
print('Fim')

print('')

q = int(input('Digite o inicio: '))
w = int(input('Digite o fim: '))
e = int(input('Digite o passo: '))
for r in range(q, w+1, e):
    print(r)
print('Fim')

print(' ')

s = 0
for a in range(0, 4):
    n = int(input('Digite um valor para ser somado: '))
    s += n
print(f'A somatória deu {s}')
print('Fim')