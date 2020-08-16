altura = int(input("Introduce la altura del cono: "))
radio = int(input("Introduce el radio de su base: "))
volumen = int(((radio ** 2) * altura * 3.1415926) // 3)
print("El volumen del cono es", volumen, "m³")