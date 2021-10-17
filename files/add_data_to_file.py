# This are going to append data to existing txt file

fichero = open("file1.txt","at") # a=append t=text file

line_to_add = "\nEsta linea se ha de añadir al fichero"

fichero.write(line_to_add)

fichero.close()