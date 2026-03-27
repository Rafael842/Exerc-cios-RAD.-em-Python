arquivo = open("frases.txt", "r")

texto = arquivo.read()

arquivo.close()

palavras = texto.split()

lista = []

for palavra in palavras:
    if palavra not in lista:
        lista.append(palavra)

print("Lista sem palavras repetidas:")
print(lista)