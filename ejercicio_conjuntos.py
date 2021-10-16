# Crear variable conjunto con 1,2,3,4,5
# Add the numbers 6,7,8,9 to the set called conjunto
# delete number 9 of the set
# verify what type is the variable conjuntof


conjunto = {1,2,3,4,5}

for i in range(6,10,1):
    conjunto.add(i)

print(conjunto)

conjunto.remove(9)

print(type(conjunto), conjunto)