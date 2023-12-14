numero = int(input("Digite um número inteiro: "))

print('Escolha sua Opção:')
print('[ 1 ] Binário')
print('[ 2 ] Octal')
print('[ 3 ] Hexadecimal')
escolha = int(input())

if escolha == 1:
    print(f"Resultado da conversão para Binário: {bin(numero)[2:]}")
elif escolha == 2:
    print(f"Resultado da conversão para Octal: {oct(numero)[2:]}")
elif escolha == 3:
    print(f"Resultado da conversão para Hexadecimal: {hex(numero)[2:]}")
else:
    resultado = "Escolha inválida"
