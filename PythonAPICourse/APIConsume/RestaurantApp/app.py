 # caminho do diretório raiz do projeto ao sys.path para que o Python possa localizar o módulo RestaurantModel
import sys
sys.path.append(r'C:\Users\leosa\PythonProjects\PythonAICourse\APIConsume')

from RestaurantModel.restaurante import Restaurante
from MenuRestaurant.food import Comida
from MenuRestaurant.drink import Bebida

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0,'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Comida('Paozinho',2.00,'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()


