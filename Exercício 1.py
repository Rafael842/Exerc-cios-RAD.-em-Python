arquivo = open("tabuada9.txt", "w")

for i in range(1, 11):
    resultado = 9 * i
    linha = f"9 x {i} = {resultado}\n"
    arquivo.write(linha)

arquivo.close()

print("Tabuada salva no arquivo tabuada9.txt")