import random
computerList=["paper","scissor","rocke"]
Computer=random.choice(computerList)
print(Computer)
thehelp=input("welcometo my app\nclice enter to strt game ro write Help to have the roal\n").capitalize()
if thehelp=="Help":
    print("""           the roals:
                1-the rocke eat the scissor
                2-the scissor eat the paper
                3-the pepar eat the rocke
                """)
else:
    user=input("""  have a choice:
                1-paper
                2-rocke
                3-scissor
                """).lower()
    if user in computerList:            
        if user==Computer:
            print("you wine")
            print(f"the Computer choice is {Computer}")
            print(f"you choice is {user}")
        else:
            print("you lose")
            print(f"the Computer choice is {Computer}")
            print(f"you choice is {user}")

            
    else:
        print ("Eror choice one of the list")
input("clice enter to Exit the app")    
