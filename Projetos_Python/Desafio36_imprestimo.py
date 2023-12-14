casa = float(input('Qual o valor da casa que você quer fazer imprestimo? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você vai pagar? '))

prestacao = casa / (anos * 12)

if salario * 0.3 < prestacao:
    print(f'Infelizmente seu imprestimo foi negado devido ao seu salario de R${salario} ser menor que 30% do valor da prestação de R${prestacao:.2f}')
else:
    print(f'Seu imprestimo foi aceito, sua casa no valor de R${casa} será paga em {anos} com prestações de R${prestacao:.2f}')