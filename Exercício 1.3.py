arquivo = open("texto.txt", "r")

texto = arquivo.read()

arquivo.close()

novo_texto = texto.replace(" ", "_")

print(novo_texto)