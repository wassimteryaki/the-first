k=6
while(k<1000000):
    p=0
    i=1
    while i<k:
        if k%i==0:
            p=p+i
            i=i+1
        else:
            i=i+1
    if p==k:
        print(p)
    k=k+1    
