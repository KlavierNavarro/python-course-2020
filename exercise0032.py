año = int(input("Dime un año: "))
def bis(x):
    if año % 4 == 0 and año % 100 != 0 or año % 4 == 0 and año % 400 == 0:
        return True
if bis(año) == True:
    print("Tiene 366 días.")
else:
    print("Tiene 365 días.")