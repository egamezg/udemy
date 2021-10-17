# Save a text file

#this returns a pointer to the file and saved to a variable
fichero = open("fileforsave.txt","wt") # Open file, create if not exist, on mode w=write and t=text

text_of_file = """
This data are going to be
saved to the text file
created with python
"""

# use the method write and pass the variable with the string to save on file
fichero.write(text_of_file)

# finally we close the file to let the other open
fichero.close()