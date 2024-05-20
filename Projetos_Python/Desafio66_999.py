soma = contador = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    contador += 1
print(f'A Soma dos {contador} valores é de {soma}')