# create dictionary with the values:
# manzana:apple, naranja:orange, platano:banana, limon:lemon
# Show the translation for naranja
# Add an element with "pina" and "pineapple"
# acreate a loop to show all the elements

dic_frutas = {"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}

print(type(dic_frutas))

print("The translation of naranja is: ", dic_frutas["naranja"])

# adding element to the dicctionary

dic_frutas["pina"] = "pineapple"

for k,v in dic_frutas.items():
    print(k,v)