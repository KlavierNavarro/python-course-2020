num1 = int(input("Dime un número: "))
num2 = int(input("Dime otro número: "))

if num2 == 0:
    print("No se puede dividir")
else:
    resto = num1 % num2
    div = num1 // num2
    print("Su división es", div)
    if resto == 0:
        print("(Exacta)")
    else:
        print("Su resto es", resto)