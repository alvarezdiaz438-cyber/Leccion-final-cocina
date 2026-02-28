class Cuchillo:
    def __init__(self, filo):
        self.filo = filo

    def atributos(self):
        print("Filo =", self.filo)

    def cortar(self, vegetal):
        if self.filo <= 0:
            print("El cuchillo no tiene filo")
        else:
            daño = 20
            vegetal.vida = vegetal.vida - daño
            self.filo = self.filo - 10
            print("Se hizo", daño, "de daño a", vegetal.nombre)
            print("Vida de", vegetal.nombre, "=", vegetal.vida)
            print("Filo actual =", self.filo)

    def afilar(self):
        self.filo = 100
        print("Cuchillo afilado a 100")

    def esta_inutil(self):
        return self.filo <= 0