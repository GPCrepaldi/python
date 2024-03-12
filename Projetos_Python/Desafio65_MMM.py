resposta = 'S'
soma = quantidade = media = maior = menor = 0

while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer Continuar [S / N]: ')).strip().upper() [0]
media = soma / quantidade

print('='*25)
print(f'Você digitou {quantidade} numeros!')
print(f'A media entre eles é de: {media}')
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')
print('='*25)
