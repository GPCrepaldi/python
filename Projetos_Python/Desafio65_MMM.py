num = int(input('Digite um valor: '))
soma = num
contador = 1
maior = menor = num
escolha = str(input('Quer continuar?(S ou N): ')).strip().upper()

while escolha == 'S':
    num = int(input('Digite mais um valor: '))
    if num > maior:
        maior = num
    else:
        menor = num
    soma += num
    contador += 1
    media = soma / contador
    escolha = str(input('Você quer continuar?(S ou N): ')).strip().upper()

print('='*25)
print(f'Você digitou {contador} numeros!')
print(f'A media entre eles é de: {media}')
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')
print('='*25)