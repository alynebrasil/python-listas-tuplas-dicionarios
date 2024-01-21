# Lista que contém as notas dos alunos
notas_alunos = [[5.0, 8.0, 6.5, 7.5],[7.0, 9.0,6.0,6.0],[4.5,5.0,6.0,10.0],[7.0,1.0,2.0,10.0], [10.0,9.5,8.5,10.0]]

# Lista para conter as médias dos alunos
medias= []

# Para as listas dentro da lista de notas dos alunos
for notas in notas_alunos:
    soma = 0 
    quantidade_notas = 0
    # Some todos os elementos dentro de cada lista e calcule quantos elementos ela contém
    for nota in notas:
        soma += nota
        quantidade_notas += 1
    
    # Calcule a média usando a soma de todos os elementos, pela quantidade de elementos na lista
    media = soma / quantidade_notas
    medias.append(media) # Armazena na lista de médias

#Contador de aprovados começando em 0
alunos_aprovados = 0

#Para cada media dentro da lista de médias, aumente 1 no contador de aprovados
#Caso a nota for maior ou igual a 7
for media in medias:
    if media >= 7.0:
        alunos_aprovados += 1

print('O número de alunos com média maior ou igual a 7.0 é: ', alunos_aprovados)