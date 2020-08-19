n = int(input("Dime un número entero positivo: ")) 
M = [] 
count = -1 
for i in range(n): 
    M.append([0] * n) 
    if M[n-1][n-1] == 0: 
        for j in range(n): 
                M[count+1][count+1] = 1 
print(M)