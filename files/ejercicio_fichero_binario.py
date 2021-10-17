# create dictionary fruits
# save into a binary file
# verify that still is a dict
import pickle

diccionario_frutas = {"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}

file = open("filetosavedict.pckl","wb")

pickle.dump(diccionario_frutas,file)

file.close()
file2 = open("filetosavedict.pckl", "rb")

file_read = pickle.load(file2)

print(file_read)

print(file_read.values())
file2.close()
