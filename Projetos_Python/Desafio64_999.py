soma = 0
quantidade = 0
num = int(input('Digite um numero (999 para sair!): '))

while num != 999:
    soma += num
    quantidade += 1
    num = int(input('Digite outro valor (999 para sair!): '))

print(f'Você digitou {quantidade} numeros e a soma entre eles é de: {soma}')