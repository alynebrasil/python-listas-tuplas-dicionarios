# Perguntas sobre o crime
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# Lista para armazenar as respostas
respostas = []

# Preenche a lista com as respostas do usuário
for pergunta in perguntas:
    resposta = input(pergunta + " (Sim/Não): ").lower()
    if resposta == "sim":
        respostas.append(True)
    else:
        respostas.append(False)

# Classificação
positivas = respostas.count(True)

if positivas == 2:
    print("Classificação: Suspeita")
elif 3 <= positivas <= 4:
    print("Classificação: Cúmplice")
elif positivas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")