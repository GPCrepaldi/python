num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

def menu():
    print('=-'*25)
    print('[ 1 ] somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair')

menu()
escolha = int(input('Sua escolha: '))

while escolha != 5:
    if escolha == 1:
        soma = num1 + num2
        print(f'A soma é: {soma}\n')
        menu()
        escolha = int(input('Faça sua escolha novamente: '))
    elif escolha == 2:
        multi = num1 * num2
        print(f'A multiplicação é: {multi}\n')
        menu()
        escolha = int(input('Faça sua escolha novamente: '))
    elif escolha == 3:
        maior = 0
        if num1 > num2:
            maior = num1
            print(f'O maior valor é: {num1}\n')
        elif num2 > num1:
            maior = num2
            print(f'O maior valor é: {num2}\n')
        else:
            print(f'Os valores são iguais...\n')
        menu()
        escolha = int(input('Faça sua escolha novamente: '))
    elif escolha == 4:
        num1 = float(input('Escolha novamente o primeiro valor: '))
        num2 = float(input('Escolha novamente o segundo valor: '))
        menu()
        escolha = int(input('Faça sua escolha novamente: '))
    else:
        print(f'Escolha inválida... tente novamente:')
        menu()
        escolha = str(input('faça sua escolha novamente: '))

print(f'Você saiu do programa, obrigado!!\n')