
nume = input ("Introduceti numele dvs. ")
tara = input ("Introduceti tara de unde sunteti: ")
age = int (input ("Introduceti varsta: "))
varsta_pensionare = 65 - age



if age <= 65:
    print (nume, "este din ", tara , "unde varsta de pensionare este 65 de anii", nume , "mai are pana la pensionare ", varsta_pensionare , "ani")
elif age >= 65:
    print (nume, "Poate iesi la pensie")
    