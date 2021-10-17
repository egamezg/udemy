# Try allow us to handle if the code has error


num1 = 5
num2 = 2
#
# This code throws an ZeroDivisionError
# division = num1 / num2

try:
    division = num1 / num2
    print(division)
except ZeroDivisionError:
    print("Division by 0 not allowed")
except TypeError:
    print("Alguno de los datos no es un número")
else:
    print("else")
# finally allow us to excute code indepened of the result, try or except
# finally executes allways
finally:
    print("Esta prueba del try se ha terminado")