DNI = input("Dime el DNI completo: ")
num = int(DNI[:8])
let = DNI[-1]
letr = let.upper()

def letra_dni(x):
    letra = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
    return letra[x % 23]
if letra_dni(num) == letr:
    print("La letra introducida coincide con el número.")
else:
    print("La letra introducida no coincide con el número.")