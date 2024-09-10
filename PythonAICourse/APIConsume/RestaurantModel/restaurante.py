import sys
sys.path.append(r'C:\Users\leosa\PythonProjects\PythonAICourse\APIConsume') 

from Avaliacao.restaurante_avaliacao import Avaliacao
from MenuRestaurant.menu_item import ItemCardapio

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
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
 
    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        exibindo_titulo = f'Cardapio do restaurante {self._nome}'
        linha_separacao = '_' * (len(exibindo_titulo) + 4)
        print(linha_separacao)
        print(exibindo_titulo)
        print(linha_separacao)
        
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item,'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome.ljust(17)} | Preço: R${str(item._preco).ljust(17)} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome.ljust(17)} | Preço: R${str(item._preco).ljust(17)} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)

