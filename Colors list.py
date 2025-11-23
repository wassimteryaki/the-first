colors=[]
while True:
    s=input ("do you want to add a color for your list\n").lower()
    if s=="yes":
        x=input ("what the color that you want to add\n")
        colors.append(x)
        print(colors)
    c=input ("do you want to remove a color from your list\n").lower()
    if c=="yes":
        v=input ("what the color that you want to remove\n")
        print (colors.remove(v))
    end=input("do you want to end the app").lower()    
    if end=="yes":
        break
