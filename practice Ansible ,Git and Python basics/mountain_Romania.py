# Mountain travel routes
from colorama import Fore, Back, Style
import webbrowser



print(" \n *** Hello Traveler ***")
print(" We have some nice track for you !")
print(Fore.GREEN + " We have 5 beautiful location for you arround the Romania with a lot of track: ")




print("\nMoldoveanu \nSureanu \nRetezat \nCalimani \nRodnei")

inpm = str(input("Please write a mountain do you want to go: "))

if (inpm == 'Moldoveanu'):
    
    webbrowser.open("https://en.wikipedia.org/wiki/Moldoveanu_Peak")
    print ("The near airport is located on Brasov")

    print("Do you want to see a maps from airport to the mountain: yes / no")
    inp3 = str(input("Do you want to see a maps from airport to the mountain: yes / no "))

    if inp3 == 'yes':
      webbrowser.open("https://www.google.com/maps/dir/V%C3%A2rful+Moldoveanu/Aeroportul+Interna%C8%9Bional+Bra%C8%99ov-Ghimbav,+Strada+Hermann+Oberth+nr.+35,+Ghimbav+507075/@45.5922435,24.8071848,10.96z/data=!4m13!4m12!1m5!1m1!1s0x474cc1a89d331d23:0x787badbc12519054!2m2!1d24.7361481!2d45.5997668!1m5!1m1!1s0x40b3516325fc26bd:0x6b2e9742cdd28ea4!2m2!1d25.5175696!2d45.6944509?entry=ttu")

    else:
      print("We can go ahead !")
      print("Can you choise another mountain")
      print("\nMoldoveanu \nSureanu \nRetezat \nCalimani \nRodnei")


if inpm == 'Sureanu':
    
     webbrowser.open("https://en.wikipedia.org/wiki/Șureanu_Mountains")
     print("The near airport is located on Sibiu")
     print("Do you want to see a maps from airport to the mountain: yes / no")
    
     inp4 = str(input("Do you want to see a maps from airport to the mountain: yes / no "))
     if inp4 == 'yes':
      webbrowser.open("https://www.google.com/maps/dir/%C8%98ureanu/Aeroportul+Interna%C8%9Bional+Sibiu,+%C8%98oseaua+Alba+Iulia+73,+Sibiu+550052/@45.8330896,23.3148332,10z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x474c2a7d4cef8f29:0xcd0399083d2a7370!2m2!1d23.2916671!2d45.691667!1m5!1m1!1s0x474c42b01b9df1e3:0x8c4b6c9fa34c9859!2m2!1d24.0944402!2d45.7890745?entry=ttu")
    
     else:
      print("We can go ahead !")
      print("Can you choise another mountain")
      print("\nMoldoveanu \nSureanu \nRetezat \nCalimani \nRodnei")

if inpm == 'Retezat':
     webbrowser.open("https://en.wikipedia.org/wiki/Retezat_Mountains")
     print("The near airport is located on Sibiu")
     inp5 = str(input("Do you want to see a maps from airport to the mountain: yes / no "))
     
     if inp5 == 'yes':
      webbrowser.open("https://www.google.com/maps/dir/Sibiu+International+Airport,+%C8%98oseaua+Alba+Iulia,+Sibiu/Masivul+Retezat/@45.6757205,23.1696186,10z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x474c42b01b9df1e3:0x8c4b6c9fa34c9859!2m2!1d24.0944402!2d45.7890745!1m5!1m1!1s0x474e0ba442a5f2b5:0x3276c299731ac972!2m2!1d22.9043242!2d45.3707365?entry=ttu")

     else: 
      print("We can go ahead !")
      print("Can you choise another mountain")
      print("\nMoldoveanu \nSureanu \nRetezat \nCalimani \nRodnei")

if (inpm == 'Calimani'):
     webbrowser.open("https://en.wikipedia.org/wiki/C%C4%83limani_Mountains")
     print("The near airport is located on Targu Mures")
     inp6 = str(input("Do you want to see a maps from airport to the mountain: yes / no "))
     if inp6 == 'yes':
        webbrowser.open("https://www.google.com/maps/dir/Mun%C8%9Bii+C%C4%83limani/Aeroportul+%E2%80%9ETransilvania%E2%80%9D+T%C3%A2rgu+Mure%C8%99,+DN15,+Ungheni/@46.8293072,23.8868151,9z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x474a0cb0544011d1:0xadb88b190a0d258!2m2!1d25.05!2d47.1166667!1m5!1m1!1s0x474bc7249e9b6957:0x992592537521a34a!2m2!1d24.4235207!2d46.4670929?entry=ttu")
     
     else:
        print("We can go ahead !")
        print("Can you choise another mountain")
        print("\nMoldoveanu \nSureanu \nRetezat \nCalimani \nRodnei")

if (inpm == 'Rodnei'):
     webbrowser.open("https://en.wikipedia.org/wiki/Rodna_Mountains")
     print("The near airport is located on Baia Mare")
     inp7 = str(input("Do you want to see a maps from airport to the mountain: yes / no "))
     if inp7 == 'yes':
        webbrowser.open("https://www.google.com/maps/dir/Mun%C5%A3ii+Rodnei/Aeroportul+Interna%C8%9Bional+Maramure%C5%9F+Baia+Mare,+Baia+Mare/@47.4849057,23.6588146,10z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x4736125b44058851:0xbaf10bbc46a481b6!2m2!1d24.556025!2d47.5340734!1m5!1m1!1s0x4737ddf7dfa1b081:0x3c461273ecdbb743!2m2!1d23.4668631!2d47.6610618?entry=ttu")
     else:
        print("We can go ahead !")
        print("Can you choise another mountain")
        print("\nMoldoveanu \nSureanu \nRetezat \nCalimani \nRodnei") 


