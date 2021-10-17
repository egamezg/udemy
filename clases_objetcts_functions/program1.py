import modulefiles

#filetoread = modulefiles.File("file2.txt")

file2 = "file3.txt"
text_to_add1 = "Primer texto al grabar\n"
text_to_add2 = "Segunda linea al hacer append\n"
test = modulefiles.File(file2)

test.savefile(text_to_add1)
test.addfile(text_to_add2)
print(test.readfile())
