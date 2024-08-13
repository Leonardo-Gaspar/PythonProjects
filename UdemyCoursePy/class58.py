# Desempacotamento em chamadas 
# de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
# p, b, *_, u = lista
# print(p,u)

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*lista)
print(*string)

print(*lista, sep='\t')