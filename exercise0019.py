num = int(input("Dime un número entero del 1 al 10: "))
if num % 2 == 0 and num % 3 ==  0:
    print("Es múltiplo de 2 y de 3")
elif num % 2 == 0 and num % 3 != 0:
    print("Es múltiplo de 2")
elif num % 2 != 0 and num % 3 == 0:
    print("Es múltiplo de 3")
else:
    print("No es múltiplo de 2 ni de 3")