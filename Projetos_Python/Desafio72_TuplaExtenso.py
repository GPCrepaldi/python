extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input('\nDigite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end=' ')

    print(f'Você digitou o número: {extenso[num]}')

    resp = str(input('\nVocê quer continuar?[S/N] ')).lower()
    if resp == 'n':
        print('Obrigado!!')
        break
    while resp != 's':
        resp = str(input('Digite "s" ou "n"' ))