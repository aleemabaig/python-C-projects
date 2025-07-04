print("Welcome to PYTHON resturant")
print("Here's the menue")
dic={"Pizza":40,
      "Pasta":50,
      "Burger": 60,
      "Salad": 70,
      "Cofee": 80}
print("Pizza :Rs 40\n"
      "Pasta :Rs 50\n"
      "Burger :Rs 60\n"
      "Salad :Rs 70\n"
      "Cofee :Rs 80\n")
ordertotal=0
you=input("Enter your first item you want to order : ")
print(f"{you} has been added")
if you in dic:
    ordertotal+=dic[you]
a= input("Do you want any other oder : ")
if a=='yes':
    b=input("Enter your second order : ")
    print(f"{b} has been added")
    if b in dic:
      ordertotal+=dic[b]
      print(f"Your total Bill is :{ordertotal}")

elif a=='no':
    print(f"Your bill is {ordertotal}")


