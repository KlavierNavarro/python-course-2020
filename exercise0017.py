contraseña = int(input("Introduzca su contraseña: "))
i = 0
while contraseña != 1234:
    print("Contraseña incorrecta. Inténtelo de nuevo. Llevas", i + 1, "intentos.")
    contraseña = int(input("Introduzca su contraseña: "))
    i += 1
print("Has accedido con éxito.")