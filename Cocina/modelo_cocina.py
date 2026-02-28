class Cocina:
    def __init__(self):
        self.inventario = ["olla", "cuchillo", "cebolla", "tomate", "pastas", "agua"]

    def verificar_objetos(self):
        if "olla" in self.inventario:
            print("La olla esta lista")
            return True
        else:
            print("No puedes iniciar sin olla")
            return False