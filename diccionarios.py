diccionario = {"red":"rojo", "blue":"azul"}

print(diccionario)

# acceso a un valor de la clave red
print(diccionario["red"])

# podemos anadir clave/valor
diccionario["black"] = "negro"

print(diccionario)

# podemos borrar valores

diccionario.pop("red")
# de esta forma tambien podemos borrar valores
# del(diccionario["red"])

print(diccionario)

# para acceder tanto a claves como valores podemos hacer lo siguiente
# con un bucle for

for clave,valor in diccionario.items():
    print(f"{clave}:{valor}")