
# This is the fisrt verion of the program, the easiest one

print("Hello, souhaite convertir de \"pouces vers cm\" ou \"cm vers pouces\" ")
i = 0
while(i==0):
    i = int(input("entrez votre choix\n1.la converssion pouces vers cm\n2.la converssion cm vers pouces\n3.fin du prgramme\n"))
    if(i==1):
        print("vous etes sur la converssion pouces vers cm ")
        val = float(input("Entrez la valeur a convertir\n"))
        valconv= val*(2.54)
        print(f"la valeur en cm est bien {valconv} cm ")
        i=0
    if(i==2):
        print("vous etes sur la converssion cm vers pouces ")
        val = float(input("Entrez la valeur a convertir\n"))
        valconv= val/(2.54)
        print(f"la valeur en pouces est bien {valconv} pouces ")
        i=0
    if(i==3):
        print("fin du prgramme")

#----------------------------------------------------------------------------------------------------------------------------------#

#This is the Full converssion program with Exeption and very detailed


"""
conversion: this function convert units from  unit1 to unit2

Return :
 True : User don't wont to convert anymore
 False : User has gave a value to convert 
"""
def conversion(unit1: str, unit2: str, fact: float):
    valeur = float(input(f"Conversion {unit1} -> {unit2}. Enter value on {unit1} (or 'q' to leave) : "))
    if valeur == "q":
        return True
    try:
        valeur_float = valeur
    except ValueError:
        print("ERROR : You have to Enter a numerique value")
        print("(Use cama not a fullstop for decinmal)")
        return conversion(unit1, unit2, fact)

    valeur_convertie = round(valeur_float * fact, 2)
    print(f"conversion result: {valeur_float} {unit1} = {valeur_convertie} {unit2}")
    return False
"""
1 inches = 2.54 cm
1 cm = 0.394 inches

Here is how the program is working
1 - Ask the user weither is looking to convert "inches to cm" or "cm vers inches"
2 - Ask the user to enter the value to convert with the unit 
3 - display the value converted 
- End of the program.
"""


while True:
    # Menu : Conversion choise
    print("This programme will let you do units conversion")
    print("1 - Inches to cm")
    print("2 - cm vers Inches")
    choise = input("Your Choise (1 ou 2): ")
    if choise == "1" or choise == "2":
        break
    print("ERROR : You have to enter 1 or 2")

while True:
    # Enter value to convert
    if choise == "1":
        if conversion("Inches", "cm", 2.54):
            break
    if choise == "2":
        if conversion("cm", "Inches", 0.394):
            break


