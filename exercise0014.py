num = int(input("Dime un número: "))
if num >= 100:
    print(num)
elif num < 100 and num >= 10:
    print("0", num, sep= "")
else:
    print("00", num, sep= "")