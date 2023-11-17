nome = input('Qual o seu nome? ')
print(f'Prazer em te conhecer {nome:=^20}!')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'a soma é {s}')
print(f'o produto é {m}\n')
print(f'a divisão é {d}')
print(f'a Divisão inteira é {di}', end=' >>> ')
print(f'a potência é {e}')