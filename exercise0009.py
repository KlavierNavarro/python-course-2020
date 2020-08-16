mmHg = int(input("Dime una cantidad de milímetros de mercurio: "))
atm = int(mmHg / 760)
pa = int(101325 * atm)
print(mmHg, "mmHg son", atm, "atmósferas y", pa, "pascales")