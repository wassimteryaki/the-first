import random
print("welcom to my app\nenter the names of your frends to chois one to pay\nshuld put comma between each name")
names=input()
names=names.split(",")
the_len=len(names)
the_rand=random.randint(0,the_len-1)
the_loser=names[the_rand]
print (the_loser)
