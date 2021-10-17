import re

texto = "Esto es un frase de pruebas para hacer busquedas"

palabra_a_buscar = "frase"

busqueda = re.search(palabra_a_buscar,texto)

print(busqueda.start())
