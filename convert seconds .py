time= int(input("enter your time by second:\n"))
#convert all by minut 
m=time//60
#from minute to:
second=(time%60)
hour= m//60
minute=m%60

print("hour= "+str(hour))
print("minute= "+str(minut))
print("second= "+str(secund))
