num = int(input("Dime un número del 1 al 7: "))
while num > 7 or num < 1:
    print("Eso no es del 1 al 7")
    num = int(input("Dime un número del 1 al 7: "))
if num == 1:
    print("Es lunes")
elif num == 2:
    print("Es martes")
elif num == 3:
    print("Es miércoles")
elif num == 4:
    print("Es jueves")
elif num == 5:
    print("Es viernes")
elif num == 6:
    print("Es sábado")
else:
    print("Es domingo")