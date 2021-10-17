import pickle

fichero = open("ficherocolores.pckl","rb")

fichero_leido = pickle.load(fichero)

print(fichero_leido)