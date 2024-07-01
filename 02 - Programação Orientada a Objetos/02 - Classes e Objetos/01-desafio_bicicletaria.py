class Bicicleta:
    # definindo os atributos
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmm.....")

    # def __str__(self):
    #     return f"Bicicleta: Cor={self.cor}, Modelo={self.modelo}, Ano={self.ano}, Valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# b1 = Bicicleta("Vermelha", "Caloi", 2022, 1982)
# b1.buzinar()
# b1.correr()
# b1.parar()
#
# print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Verde", "Monark", 2000, 1839)
b2.buzinar()  # = Bicicleta.buzinar(b2)

print(b2)
