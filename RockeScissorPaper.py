from termcolor import colored, cprint
import random
computerList=["paper","scissor","rocke"]
Computer=random.choice(computerList)
thehelp=input("welcometo my app\nclice enter to start game ro write Help to have the roal\n").capitalize()
if thehelp=="Help":
    print("""           the roals:
                1-the rocke eat the scissor
                2-the scissor eat the paper
                3-the pepar eat the rocke
                """)
                
ta_com=0
ta_us=0
            
while True:
    user=input("""  have a choice:
            1-paper
            2-rocke
            3-scissor
            """).lower()
    if user in computerList:
        if user==Computer :
            cprint ("no winner and no Loser",'yellow')
        elif user=="paper" and Computer=="rocke":
            cprint("you wine",'green')
            ta_us=ta_us+1
        elif user=="rocks"and Computer=="scissor":
            cprint("you wine",'green')
            ta_us=ta_us+1
        elif user=="scissor"and Computer=="paper":
            cprint("you wine",'green')
            ta_us=ta_us+1
        else:    
            cprint("you lose",'red')
            ta_com=ta_com+1
        print(f"the Computer choice is {Computer}")
        print(f"you choice is {user}")
        print(f"your score is:{ta_us}")
        print(f"the Computer score is{ta_com}")
    
                
    else:
        cprint ("Eror choice one of the list",'red')
    repit= input("do you want to repit the Game?\nyes or no?").lower() 
    if repit=="no":
        if ta_com>ta_us:
            cprint (f"you Lose({ta_us},{ta_com})",'red')
        if ta_com<ta_us:
            cprint(f"you Win ({ta_us},{ta_com})",'red')
        if ta_com>0 or ta_us>0:
            
            if ta_com==ta_us:
                print (f"no winner no Loser({ta_us},{ta_com})")
        
        input("clice enter to Exit the app")        
        break
    

