# create function that takes 3 nums and divde the first with the substraction
# of the second and the third

def operacion(num1,num2,num3):
    try:
        return num1 / (num2 - num3)
    except ZeroDivisionError:
        print("División por cero")



print(operacion(5,4,2))
print(operacion(6,3,3))