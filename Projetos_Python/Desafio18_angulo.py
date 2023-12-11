import math

angulo = float(input('Digite um valor: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'o valor {angulo}, tem o seno de {seno:.2f} e o cosseno de {cosseno:.2f} e a tangente é {tangente:.2f}')
