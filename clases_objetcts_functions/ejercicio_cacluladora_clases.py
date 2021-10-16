# Create a calculator with (suma/resta/multipliacion y division)
# Que pida numero, operador y numero y dependiendo del operador realice una u otra cosa

class Calculadora:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def Sumar(self):
        return self.num1 + self.num2

    def Restar(self):
        return self.num1 - self.num2

    def Multi(self):
        return self.num1 * self.num2

    def Divi(self):
        return self.num1 / self.num2

numA = int(input("Introduce un número: "))
oper = input("Introduce la operacion a realizar: +, -, *, / ")
numB = int(input("Introduce el segundo número: "))

user = Calculadora(numA,numB)

if oper == "+":
    print(user.Sumar())
elif oper == "-":
    print(user.Restar())
elif oper == "*":
    print(user.Multi())
elif oper == "/":
    print(user.Divi())
else:
    print("El operador no se encuentra")