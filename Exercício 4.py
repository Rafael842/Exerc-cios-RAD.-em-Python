nome = input("Nome do aluno: ")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

arquivo = open("resultado_aluno.txt", "w")

arquivo.write(f"Aluno: {nome}\n")
arquivo.write(f"Média: {media}\n")
arquivo.write(f"Situação: {resultado}\n")

arquivo.close()

print("Resultado salvo no arquivo resultado_aluno.txt")