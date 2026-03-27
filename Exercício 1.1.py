arquivo = open("dna.txt", "r")

dna = arquivo.read().strip()

arquivo.close()

dna_inverso = dna[::-1]

print("DNA original:", dna)
print("DNA inverso:", dna_inverso)