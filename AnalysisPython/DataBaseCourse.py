acessorios_passat = {
    'Rodas de Liga',
    'Travas Elétricas',
    'Piloto Automático',
    'Central Multimídia'}

acessorios_crossfox = {
    'Piloto Automático',
    'Teto Panorâmico',
    '4 X 4',
    'Central Multimídia'}

acessorios_jetta = {
    'Controle de Estabilidade',
    'Câmbio Automático',
    'Travas Elétricas',
    'Rodas de Liga'}


#DISJUSÇÃO
print(set.isdisjoint(acessorios_passat, acessorios_crossfox))

#INTERSEÇÃO
print(acessorios_passat & acessorios_crossfox)

print(acessorios_passat & acessorios_jetta)

print(set.intersection(acessorios_passat, acessorios_crossfox))

print(set.intersection(acessorios_passat, acessorios_crossfox, acessorios_jetta))

#UNIÃO
print(acessorios_passat | acessorios_crossfox)

print(set.union(acessorios_passat,acessorios_crossfox,acessorios_jetta))

print(set.union(acessorios_passat,acessorios_crossfox,acessorios_jetta, {'Teto Solar'}))
#------------------------------------------------------------------------------------------------------------------------------------------------


carros = {
    'Crossfox',
    'Dodge Journey',
    'Jetta Variant',
    'Passat'
}

print('Crossfox' in carros)

#PERFORMANCE WITH A BUNCH OF ELEMENTS

elementos_set = set(range(10000))
elementos_list = list(range(10000))
elementos_tuple = tuple(range(10000))


def verificar_elementos_in(elemento_iteravel):
    """Verifica se cada número no intervalo especificado pertence ao iteravel 'elemento_iteravel'"""

    for i in range(10000):
        if i in elemento_iteravel:
            pass

print("Tempo de execução set: ")

# %time verificar_elementos_in(elementos_set)
# print("="*30)
#
# %time verificar_elementos_in(elementos_list)
# print("="*30)
#
# %time verificar_elementos_in(elementos_tuple)
# print("="*30)