# Read file the text file1.txt

# This gives back the data and saves into a variable
fichero = open("file1.txt","rt") # This open file in r=read mode and t=text file

# We read the content and store again in a variable
datos_fichero = fichero.read()

#We print the content of the variable with readed data of file
print(datos_fichero)