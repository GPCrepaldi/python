salario = float(input('Digite o valor do seu salario: '))

if salario > 1250:
    aumento = salario * 1.1
else:
    aumento = salario * 1.15

print(f'O seu salario com o aumento será de: R${aumento:.2f}')
