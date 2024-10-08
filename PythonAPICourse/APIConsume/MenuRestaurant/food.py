import sys
sys.path.append(r'C:\Users\leosa\PythonProjects\PythonAICourse\APIConsume') 

from MenuRestaurant.menu_item import ItemCardapio

class Comida(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao
        
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)

