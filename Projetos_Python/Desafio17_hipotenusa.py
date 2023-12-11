from math import sqrt, hypot

cateto1 = float(input('Digite o valor do primeiro cateto: '))
cateto2 = float(input('Digite o valor do segundo cateto: '))

hipotenusa1 = sqrt(cateto1**2 + cateto2**2)
hipotenusa2 = hypot(cateto1, cateto2)

print(f'Este triângulo tem uma hipotenusa de: {hipotenusa1:.2f}')
print(f'Este triângulo tem uma hipotenusa de: {hipotenusa2:.2f}')
