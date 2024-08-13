class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Mamifero(Animal):
    def __init__(self, nome, idade, habitat):
        super().__init__(nome, idade)
        self.habitat = habitat

class Aves(Animal):
    def __int__(self, nome, idade, canto_ave):
        super().__init__(nome, idade)
        self.canto_ave = canto_ave

class Cachorro(Mamifero):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade, "Terra")
        self.raca = raca

    def emitir_som(self):
        return f"{self.nome} está latindo."

meu_cachorro = Cachorro("Zouk", 8, "Yorkshire")
print(meu_cachorro.emitir_som())

class Gato(Mamifero):
    def __init__(self, nome, idade, cor_pelo):
        super().__init__(nome, idade, "Terra")
        self.cor_pelo = cor_pelo

    def emitir_som(self):
        return f"{self.nome} está miando."


meu_gato = Gato("Jeromel", 5, "Laranja Listrado")
print(meu_gato.emitir_som())

class Primata(Mamifero):
    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade, "Savana")
        self.especie = especie

    def bater_no_peito(self):
        return f"{self.nome} está batendo no peito."


meu_primata = Primata("Jaime", 9, "Gorila")
print(meu_primata.bater_no_peito())

class Ariranha(Mamifero):
    def __init__(self, nome, idade, tamanho_das_manchas):
        super().__init__(nome, idade, "Cerrado")
        self.tamanho_das_manchas = tamanho_das_manchas

    def tamanho_mancha(self):
        return f"{self.nome} tem a mancha de tamanho {self.tamanho_das_manchas} e vive na {self.habitat}."

minha_ariranha = Ariranha("Olivia", 4, "mediano")
print(minha_ariranha.tamanho_mancha())

class Hipopotamo(Mamifero):
    def __init__(self, nome, idade, tamanho_presa):
        super().__init__(nome, idade, "Savana Africana")
        self.tamanho_presa = tamanho_presa

    def tamanho_da_presa(self):
        return f"{self.nome} tem a mancha de tamanho {self.tamanho_presa} e vive na {self.habitat}."

meu_hipopotamo = Hipopotamo("Jefersson", 12, "grande")
print(meu_hipopotamo.tamanho_da_presa())

class Bem_te_vi(Aves):
    def __init__(self, nome, idade, qnt_canto):
        super().__init__(nome, idade)
        self.qnt_canto = qnt_canto

    def quantidade_canto(self):
        return f"{self.nome} tem a idade {self.idade} e seu canto {self.qnt_canto} por dia. "

meu_bem_te_vi = Bem_te_vi("Mordecai", 3, "242")
print(meu_bem_te_vi.quantidade_canto())

class Tucano(Aves):
    def __init__(self, nome, idade, tamanho_bico):
        super().__init__(nome, idade)
        self.tamanho_bico = tamanho_bico

    def tamanho_do_bico(self):
        return f"{self.nome} tem a idade {self.idade} e seu bico tem {self.tamanho_bico}. "

meu_tucano= Tucano("Soleil", 4, "24cm")
print(meu_tucano.tamanho_do_bico())

class Falcao(Aves):
    def __init__(self, nome, idade, envergadura):
        super().__init__(nome, idade)
        self.envergadura = envergadura

    def envergadura_falcao(self):
        return f"{self.nome} tem a idade {self.idade} e sua envergadura tem {self.envergadura}. "

meu_falcao= Falcao("Timão", 6, "166cm")
print(meu_falcao.envergadura_falcao())

class Avestruz(Aves):
    def __init__(self, nome, idade, velocidade):
        super().__init__(nome, idade)
        self.velocidade = velocidade
    def velocidade_media(self):
        return (f"{self.nome} tem a idade {self.idade} e tem media de {self.velocidade}.")
meu_avestruz = Avestruz("Aerado", 7, "70km/h")
print(meu_avestruz.velocidade_media())

class Pavao(Aves):
    def __init__(self, nome, idade, qnt_cores):
        super().__init__(nome, idade)
        self.qnt_cores = qnt_cores

    def quantidade_cores(self):
        return (f"{self.nome} tem a idade {self.idade} e tem {self.qnt_cores} cores em suas penas.")
meu_pavao = Pavao("Girafales", 11, 4)
print(meu_pavao.quantidade_cores())