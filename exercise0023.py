filas = int(input("Dime el número de filas: "))
columnas = int(input("Dime el número de columnas: "))

A = []
for i in range(filas):
    A.append([0] * columnas)
B = []
for i in range(filas):
    B.append([0] * columnas)
print("Lectura de la matriz A")
for i in range(filas):
    for j in range(columnas):
        A[i][j] = float(input("Componente ({0},{1}): ".format(i, j)))

print("Lectura de la matriz B")
for i in range(filas):
    for j in range(columnas):
        B[i][j] = int(input("Componente ({0},{1}): ".format(i, j)))

C = []
for i in range(filas):
    C.append([0] * columnas)

for i in range(filas):
    for j in range(columnas):
        C[i][j] = A[i][j] - B[i][j]

print("Resta:")
for i in range(filas):
    for j in range(columnas):
        print(C[i][j], end=" ")
    print()