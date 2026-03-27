arquivo = open("dados_pessoa.txt", "r")

linhas = arquivo.readlines()

arquivo.close()

lista = []

for linha in linhas:
    lista.append(linha.strip())

print("Conteúdo do arquivo dentro da lista:")
print(lista)