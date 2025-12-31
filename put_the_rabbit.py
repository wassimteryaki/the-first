line1=["g","g","g"]
line2=["g","g","g"]
line3=["g","g","g"]
strlocation=input("enter the location that you want to the rabbit in\n")
intlocation=int(strlocation)


if strlocation[0]=="1":
    line1.remove(line1[int(strlocation[1])-1])
    line1.insert(int(strlocation[1])-1,"r")
    
if strlocation[0]=="2":
    line2.remove(line2[int(strlocation[1])-1])
    line2.insert(int(strlocation[1])-1,"r")    
if strlocation[0]=="3":
    line3.remove(line3[int(strlocation[1])-1])
    line3.insert(int(strlocation[1])-1,"r")    
print(line1)    
print(line2)    
print(line3)    


input("clicke enter to closs the app")
