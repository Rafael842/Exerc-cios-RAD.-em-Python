arquivo = open("texto.txt", "r")

texto = arquivo.read()

arquivo.close()

palavras = texto.split()

quantidade = len(palavras)

print("Quantidade de palavras:", quantidade)