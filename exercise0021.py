n = int(input("Dime un número entero positivo: ")) 
M = [] 

for i in range(n): 
    M.append([0] * n) 

count = 0
for j in range(n):
    M[count][count] = 1
    count += 1
print(M)