nome = str(input('Digite algum nome: ')).strip().lower()

print(f'A letra A aparece {nome.lower().count("a")} vezes')
print(f'A primeira vez que aparece é na posição {nome.lower().find("a")}')
print(f'A ultima vez que aparece é na posição {nome.lower().rfind("a")}')
