# Un conjunto es un set

conjunto_de_colores = {"rojo", "verde", "azul"}

# No se puede acceder a un indice porque son colecciones desordenadas
# conjunto_de_colores[0]

for i in conjunto_de_colores:
    print(i)

print(len(conjunto_de_colores))

conjunto_de_colores.add("negro")

print(conjunto_de_colores)


conjunto_de_colores.remove("verde")

print(conjunto_de_colores)