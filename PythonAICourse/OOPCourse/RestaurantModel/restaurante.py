import sys
sys.path.append(r'c:\Users\leosa\PythonProjects\PythonAICourse\OOPCourse')

from Avaliacao.restaurante_avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):       
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        exibindo_titulo = f'{"Nome do Restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Avaliação".ljust(19)} | {"Status"}'
        linha_separacao = '_' * (len(exibindo_titulo) + 4)
        print(linha_separacao)
        print(exibindo_titulo)
        print(linha_separacao)
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)}| {restaurante.ativo}')
        print()
        
    @property
    def ativo(self):
        return '✓' if self._ativo else '☓'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        print(f'O restaurante {self._nome} está {self._ativo}')
        
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
     
    @property   #Property faz com que a função seja capaz de ler as informações
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'  
        media_avaliacoes = round(sum(avaliacao._nota for avaliacao in self._avaliacao) / len(self._avaliacao), 1)
        return media_avaliacoes

        
    
    
            