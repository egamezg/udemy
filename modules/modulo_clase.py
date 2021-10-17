class Coche:
    def __init__(self,marca,motor,combustible,cilindrada):
        self.marca = marca
        self.motor = motor
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrar_caracteristicas(self):
        print(f"Marca: {self.marca}, Motor: {self.motor}, Combustible: {self.combustible}, Cilindrada: {self.cilindrada}")


media = lambda num1, num2, num3: (num1 + num2 + num3) / 3