"""
Cuidados com dados mutáveis
- copiando valor (imutáveis)
- apontando para o mesmo valor na memória (mutável)
"""


# lista_a = ['Luiz', 'Maria']
# lista_b = lista_a

# lista_a[0] = 'Qualquer coisa'
# print(lista_b)

lista = ['Maria', 'Helena', 'José']
lista.append('João')
i = 0
for nome in lista:
    print(i, ": ",nome)
    i+=1
    
lista2 = ['Maria', 'Helena', 'José']
lista2.append('João')
indices = range(len(lista2))
for indice in indices:
    print(indice, lista[indice])