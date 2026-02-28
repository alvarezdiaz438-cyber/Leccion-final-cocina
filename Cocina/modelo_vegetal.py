class Vegetal:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "esta completamente picado")


class Cebolla(Vegetal):
    pass


class Tomate(Vegetal):
    pass