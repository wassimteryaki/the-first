
import random 
s= input("enter the way that you want to play:\n1_randint\n2_random\n")
if s=="1" or s=="2":
    p=int(input ("enter your gass by four number:\n"))
    if p>9999 or p<1000:
        print ("eror")
    else:    
        if s=="1":
            if p==random.randint(1000,9999):
                print("you win")
            else:
                print ("you lose")
        if s=="2":
            if p==random.random()*1000:
                print("you win")
            else:
                print("you lose")
else:
    print("eror")
     
   

    
