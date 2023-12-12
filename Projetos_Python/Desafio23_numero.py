num = int(input('Digite um numero de 0 a 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Milhar {m}')
print(f'Centenas {c}')
print(f'Dezenas {d}')
print(f'Unidade {u}')
