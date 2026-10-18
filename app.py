# Pesquisa de Satisfação - TudoWeb
# Marcello Reis de Campos Melo

print("PESQUISA DE SATISFAÇÃO - TUDOWEB")

excelente = 0
bom = 0
ruim = 0

continuar = "S"

while continuar.upper() == "S":

    # Entrada de dados
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    print("\nComo você avalia nosso atendimento?")
    print("1 - Excelente")
    print("2 - Bom")
    print("3 - Ruim")

    opiniao = int(input("Escolha uma opção e confirme: "))

    # Validação da resposta
    while opiniao not in (1, 2, 3):
        print("Sua opinião é muito importante!")
        opiniao = int(input("Escolha uma opção: 1, 2 ou 3: "))

    # Processamento
    if opiniao == 1:
        avaliacao = "Excelente"
        excelente += 1

    elif opiniao == 2:
        avaliacao = "Bom"
        bom += 1

    else:
        avaliacao = "Ruim"
        ruim += 1

    # Saída individual
    print("\n=== RESUMO DA PESQUISA ===")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Avaliação: {avaliacao}")
    print("Agradecemos pela sua contribuição!")

    continuar = input("\nDeseja cadastrar outra resposta? (S/N): ")

# Resultado final
print("\n=== RESULTADO FINAL DA PESQUISA ===")
print(f"Excelente: {excelente}")
print(f"Bom: {bom}")
print(f"Ruim: {ruim}")
print(f"Total de respostas: {excelente + bom + ruim}")