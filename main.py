'''
stone =-1
paper = 1
scissor = 0
'''

import random
computer=random.choice([1,0,-1])
youstr=input("Enter Your Choice : ")
dic={"st":-1,"p": 1,"se":0}
reversedic={-1:"Stone",1:"Paper",0:"Scissor"}
you=dic[youstr]
print(f"You choose : {reversedic[you]}")
print(f"Computer choose : {reversedic[computer]}")

if(computer==you):
    print("Its a draw")
else:
    if(computer==-1 and you==1): 
        print("You Win")
    elif(computer==-1 and you==0):
        print("You Loose")
    elif(computer==1 and you==-1):
        print("You  Loose")
    elif(computer==1 and you==0):
        print("You Win")
    elif(computer==0 and you==-1):
        print("You Win")
    elif(computer==0 and you==1):
        print("You Loose")
    else:
        print("Something Went Wrong")
    

    


