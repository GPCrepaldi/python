# Inicializar variáveis
pessoas = []
idade_total = 0
maior_idade = 0
nome_mais_velha = None
mulheres_abaixo_20 = []

# Loop para ler informações de 4 pessoas
for i in range(1, 5):
    print(f'================ {i}ª Pessoa ================')
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ").upper().strip()

    # Atualizar idade total para calcular a média posteriormente
    idade_total += idade

    # Verificar se a pessoa é a mais velha
    if idade > maior_idade:
        maior_idade = idade
        nome_mais_velha = nome

    # Verificar se a pessoa é mulher e tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_abaixo_20.append(nome)

# Calcular a média de idades
media_idades = idade_total / 4

# Imprimir os resultados
print(f"\nNome da pessoa mais velha: {nome_mais_velha}")
print(f"Média de idades: {media_idades:.2f}")
print(f"Mulheres abaixo de 20 anos: {', '.join(mulheres_abaixo_20)}")
