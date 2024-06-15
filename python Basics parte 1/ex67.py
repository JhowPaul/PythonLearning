#Write a Python program to convert pressure in kilopascals to pounds per square inch,
#a millimeter of mercury (mmHg) and atmosphere pressure.
kilopascal=float(input("Insira a pressão em kilopascal: "))
psi = kilopascal / 6.89475729
mmhg = kilopascal * 760 / 101.325
atm = kilopascal / 101.325
print("The pressure in pounds per square inch: %.2f psi"  % (psi))
print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
print("Atmosphere pressure: %.2f atm." % (atm))