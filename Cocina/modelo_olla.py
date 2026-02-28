class Olla:
    def __init__(self):
        self.ingredientes = []

    def agregar(self, ingrediente):
        self.ingredientes.append(ingrediente)
        print(ingrediente, "agregado a la olla")

    def servir(self):
        print("La pasta ha sido servida con exito")