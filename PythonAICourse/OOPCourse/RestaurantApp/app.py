import sys
sys.path.append(r'c:\Users\leosa\PythonProjects\PythonAICourse\OOPCourse') # caminho do diretório raiz do projeto ao sys.path para que o Python possa localizar o módulo RestaurantModel

from RestaurantModel.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Leo', 3)
restaurante_praca.receber_avaliacao('Gui', 2)
restaurante_praca.receber_avaliacao('Emy', 4)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
    