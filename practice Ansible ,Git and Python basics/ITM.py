# For the Submissions I need to connect with the cod a sensor, I can't do that theoretically and is more advance. 
# I keep the code simple as I can.

print (" Welcome on Bank \n")

sold = 5000;

print (" Please insert option do you want below : ")
print ("1. Balance query")
print ("2. Cash withdrawal")
print ("3. Submissions\n")

key = int (input())


if key == 1:
    print (" You enter Balance query: ")
    print ("Your balance is ", sold, " $")
    print (" Do you want another option ? yes / no")
    x = (input())
    if x == 'yes':
       print (" Please insert a option bellow : ")
       print ("1. Balance query")
       print ("2. Cash withdrawal")
       print ("3. Submissions")
    if x == 'no':
       print (" We wish a nice day ! ") 
       quit()  
if key == 2:
      print ("You enter Cash withdrawal ")
      suma =  int (input (" Enter sum that you want to whitdrawal: "))
      print (" You withdrawal ", suma , " your sold is :", sold - suma, " $")
      print (" We wish a nice day !  ")
      quit() 
if key == 3:
    print ("You enter Submissions")
    print (" Please insert money in slot bellow: ")
    print (" You insert " , sold, " $" )   
    print (" We wish a nice day ! ") 
    quit()  
    
key2 = int (input())

if key2 == 1: 
     print ("You enter Balance query: ")
     print ("Your equity is ", sold, " $")
     print (" We wish a nice day ! ") 
     quit()  

if key2 == 2:
    print ("You enter Cash withdrawal ")
    suma2 =  int (input (" Enter sum that you want to whitdrawal: "))
    print (" You withdrawal ", suma2 , " your sold is", sold - suma2, " $")
    print (" We wish a nice day ! ")
    quit()

if key2 == 3:
    print ("You enter Submissions")
    print (" Please insert money in slot bellow: ")
    print (" You insert ... your equity is" , sold, " $" )
    print (" We wish a nice day ! ")
    quit() 