"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321

string = 'ABCDE'  # 5 caracteres (len)
lista = [10, 20, 30, 40]
lista[2] = 300
del lista[2]
lista.append(50)
lista.pop()
lista.append(60)
print(lista)