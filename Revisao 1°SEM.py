# Tupla:
# t = (1, 2, 3)

# Lista:
# l = [1, 2, 3]

# operações prmitidas, pois estamos acessando e utilizando o conteúdo:

# t[1]*1
# l[1]*1

# operação não prmitida para tupla:
# t[1] = 6
#

# A busca em uma array/vetor/lista ordenada
# l =[23, 43, 2, 0, 23432]
# l.sort() # a lista foi ordnada do menor para o maior
# print(l) # imprime a lista ordenada do modo crescente
#
# l.sort(reverse=True) # a lista foi ordenada do maior para o menor
# print(l) # imprime a lista ordenada do modo decrescente
#
# l = ["joão", "Mirella", "Natan", "Clara"]
# for i, name in enumerate(l):
#     if name == "Mirella":
#         break
# print("Mirella esta na posição", i)
#
# l.index("Mirella")

##DICIONÁRIO
# key -> value

# d= {"joão": xxx,
#     "Mirella": xxx,
#     "Natan": xxx,
#     "Clara": xxx,
# }
#
# notas = {
#     "joão": 7,
#     "Mirella": 5,
#     "natan": 9,
#     "Clara": 10
# }
# print(notas["natan"])
#
# rm_aluno = {
#     123: "joão",
#     124: "Clara",
#     125: "Mirella",
#     126: "Natan",
# }
# print(rm_aluno[123])
#
# # alterando valor dada uma chave
#
# rm_aluno[(123)] = "joão vitor"
# print(rm_aluno[123])

#removendo um valor do dicionário

# del rm_aluno[(123)] # Apenas apaga o registro
# ou
# rm_aluno.pop((123)) # Apaga e retorna o registro
