# Pesquisa de Satisfação - TudoWeb
# Marcello Reis de Campos Melo

print("=== PESQUISA DE SATISFAÇÃO - TUDOWEB ===")

# Entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print("\nComo você avalia nosso atendimento?")
print("1 - Excelente")
print("2 - Bom")
print("3 - Ruim")
opiniao = int(input("Escolha uma opção e confirme: "))

# Processamento
while opiniao not in (1, 2, 3):
    print("Sua opinião é muito importante!")


opiniao = int(input("Escolha uma opção: 1, 2 ou 3: "))


if opiniao == 1:
    avaliacao = "Excelente"

elif opiniao == 2:
    avaliacao = "Bom"

else:
    avaliacao = "Ruim"

#Saída
print("\n=== RESUMO DA PESQUISA ===")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Avaliação: {avaliacao}")
print("Agradecemos pela sua contribuição!")
