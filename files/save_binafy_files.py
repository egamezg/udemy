# We import module of pickle, this allow us to save on binay files
import pickle

lista = ["azul", "verde", "rojo", "amarillo"]

# crete pointer to opened file in variable fichero
fichero = open("ficherocolores.pckl", "wb")

# Save using pickle.dump the list into the file
pickle.dump(lista,fichero)

# finally close the file    
fichero.close()