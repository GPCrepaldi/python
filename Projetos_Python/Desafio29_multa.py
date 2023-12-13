velocidade = int(input('Digite a velocidade do seu carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Seu carro foi multado em R${multa:.2f} por estar acima da velocidade!!!')
else:
    print('Você estava dentro dos limites de velocidade!')
