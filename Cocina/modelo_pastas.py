class Pastas:
    def __init__(self):
        self.vida = 0

    def hervir(self):
        self.vida = self.vida + 20
        print("Nivel de coccion =", self.vida)

    def listas(self):
        return self.vida >= 100