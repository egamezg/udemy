# create variable diccionario with the following values
# key=uno   value=one
# key=dos   value=two
# key=tres  value=three
# Then add nes element to the diccionario
# key=cuatro    value=four
# Pick value from input and save as dato
# Use dato as key to paick the value on the diccionario


diccionario = {"uno":"one", "dos":"two", "tres":"three"}
print(type(diccionario), diccionario)

diccionario["cuatro"] = "four"

print(diccionario)

dato = input("introduce un numero escrito: ")

print(diccionario[dato])