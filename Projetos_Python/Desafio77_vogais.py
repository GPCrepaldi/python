#tupla contendo as palavras que serão analisadas
palavra = ('cafe', 'leite', 'pao', 'carne', 'comida')

#criada uma variável para identificar as vogais
vogais = "aeiou"

#percorrendo cada palavra da tupla
for palavra in palavra:
    print(f'\nNa palavra {palavra.upper()} temos: ', end=' ') #o end=' ' é para que a linha n seja quebrada altomaticamente

    #Verificando vogais em cada palavra
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ') #neste caso, é para que cada vogal apareça na frente, sem haver quebra de linha