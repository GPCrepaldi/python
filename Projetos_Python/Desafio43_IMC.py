peso = float(input('Digite o seu Peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / altura ** 2

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f}... Você está abaixo do peso!!!')
elif imc <= 25:
    print(f'Seu IMC é de {imc:.2f}... Você está com o peso ideal, parabens!!!')
elif imc <= 30:
    print(f'Seu IMC é de {imc:.2f}... Você está com sobrepeso!!!')
elif imc <= 40:
    print(f'Seu IMC é de {imc:.2f}... Você está com Obesidade!!!')
else:
    print(f'Seu IMC é de {imc:.2f}... Você está com Obesidade Morbida!!!! CUIDADO!!!')
    