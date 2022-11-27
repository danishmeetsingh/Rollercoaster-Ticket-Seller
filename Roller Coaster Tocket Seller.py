print("Welcome to the Rollercoaster")
height = int(input("What is your height(in cm)?"))

if height >= 120:
  print("Welcome to the Rollercoaster")
  age = input("What is your age?")
  if int(age) < 12:
    bill = 18
    print("Child Ticket.Please pay $18")
  elif int(age) <= 18:
    bill = 24
    print("Teen Ticket.Please pay $24")
  elif int(age)>= 45 and int(age)<= 55:
    print("Free Ticket on us.")
  else:
    bill = 30
    print("Adult Ticket.Please pay $30")
  wants_pic = input("Do you want to take a Picture of yours in Rollercoaster?($3) Y or N ")
  if wants_pic == "Y":
    bill += 3
    print(f"Your final bill is ${bill}")
  elif wants_pic == "y":
    bill += 3
    print(f"Your final bill is ${bill}")
  elif wants_pic == "N":  
    print("Enjoy your ride.")
  elif wants_pic == "n":
    print("Emjoy your ride")
  else:
    print("Invalid Option")
  
else:
  print("Sorry, You have to grow taller") 