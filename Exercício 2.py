from datetime import datetime

nome = input("Digite o nome: ")
rg = input("Digite o RG: ")
cpf = input("Digite o CPF: ")
ano = int(input("Digite o ano de nascimento: "))

ano_atual = datetime.now().year
idade = ano_atual - ano

arquivo = open("dados_pessoa.txt", "w")

arquivo.write(f"Nome: {nome}\n")
arquivo.write(f"RG: {rg}\n")
arquivo.write(f"CPF: {cpf}\n")
arquivo.write(f"Ano de nascimento: {ano}\n")
arquivo.write(f"Idade: {idade}\n")

arquivo.close()

print("Dados salvos no arquivo dados_pessoa.txt")