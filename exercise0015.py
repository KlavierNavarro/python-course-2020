num1 = int(input("Dime un número entero: "))
num2 = int(input("Dime otro número entero: "))
if num1 > 0 and num2 > 0:
    print("Son números positivos")
elif num1 > 0 and num2 < 0:
    print("El primero es positivo y el segundo es negativo")
elif num1 < 0 and num2 > 0:
    print("El primero es negativo y el segundo es positivo")
else:
    print("Son números negativos")