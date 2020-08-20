n = int(input("Dime un número entero positivo: "))
M = []
for i in range(n):
    M.append([0] * n)
for j in range(n):
    M[j][j] = 1
print(M)