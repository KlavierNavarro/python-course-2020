num1 = int(input("Dime un número entero: "))
num2 = int(input("Dime otro número entero: "))
if num1 > 0 and num2 > 0:
    print("Números positivos: 2")
elif num1 > 0 and num2 < 0:
    print("Números positivos: 1")
elif num1 < 0 and num2 > 0:
    print("Números positivos: 1")
else:
    print("Números positivos: 0")