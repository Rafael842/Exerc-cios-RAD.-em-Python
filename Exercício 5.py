num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

arquivo = open("calculadora.txt", "w")

arquivo.write(f"Números: {num1} e {num2}\n")
arquivo.write(f"Soma: {soma}\n")
arquivo.write(f"Subtração: {sub}\n")
arquivo.write(f"Multiplicação: {mult}\n")
arquivo.write(f"Divisão: {div}\n")

arquivo.close()

print("Resultados salvos no arquivo calculadora.txt")