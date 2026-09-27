print("=== PESQUISA DE SATISFAÇÃO - TUDOWEB ===")

# Contadores
excelente = 0
bom = 0
ruim = 0
total = 0
continuar = "S"

while continuar.upper() == "S":

# Entrada
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print("\nAvalie nosso atendimento:")
print("1 - Excelente")
print("2 - Bom")
print("3 - Ruim")
opiniao = int(input("Escolha uma opção: "))
while opiniao not in (1, 2, 3):
    print("Opção inválida!")
opiniao = int(input("Escolha 1, 2 ou 3: "))

# Processamento
if opiniao == 1:
    excelente += 1
elif opiniao == 2:
    bom += 1
else:
    ruim += 1
total += 1

continuar = input("\nDeseja registrar outra resposta? (S/N): ")

# Relatório final
print("\n=== RESULTADO DA PESQUISA ===")
print(f"Total de participantes: {total}")
print(f"Excelente: {excelente}")
print(f"Bom: {bom}")
print(f"Ruim: {ruim}")
if total > 0:
    print("\nPercentuais:")

print(f"Excelente: {excelente/total*100:.1f}%")
print(f"Bom: {bom/total*100:.1f}%")
print(f"Ruim: {ruim/total*100:.1f}%")
print("\nObrigado pela participação de todos!")