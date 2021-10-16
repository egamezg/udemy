# Class/Constructor that has properties
class ClaseSilla:
    color = "blanco"
    precio  = 100

# Create object, from the class, is a instance of the class
objetoSilla1 = ClaseSilla()


print(objetoSilla1.color)

objetoSilla2 = ClaseSilla()

objetoSilla2.color = "verde"
objetoSilla2.precio = 120


print(objetoSilla2.precio)


class Persona:
    def __init__(self,nombre,edad):
        self.nombre  = nombre
        self.edad = edad

    def saludar(self):
        print("hola, me llamo {}, y tengo {}".format(self.nombre,self.edad))


persona1 = Persona("juan",37)

print(persona1.edad)
print(persona1.nombre)

persona1.saludar()