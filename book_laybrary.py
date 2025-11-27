labrary=[]
wish_book=[]
real_book1=input("what is the book that you have in your library\n")
if real_book1 :
    labrary.append(real_book1)
    real_book2=input("and what\n")
    if real_book2:
        labrary.append(real_book2)
    
print (f"you just have{labrary}")
imaging_book1=input("do you want to bay some in the fuotar\n").lower()
if imaging_book1=="yes":
    imaging_book1=input("what its\n")
    if imaging_book1:
        wish_book.append(imaging_book1)
    else :
        print ("Good wish but we cant add it to the list ")
    imaging_book2=input("and what?\n")
    if imaging_book2:
        wish_book.append(imaging_book2)
    print(wish_book)    
questione=input("what about now \ndid you by any book from the book that you hobe to have") 
if questione=="yes" or questione=="of cours":
    real_book3=input("what its\n")
    if real_book3:
        labrary.append(real_book3)
    elif real_book3 in wish_book:    
        wish_book.remove(real_book3)
    print (f"you just have{labrary}")

    print(f"you should to by {wish_book}")     
questione=input("did you seal some ?\n") 
if questione=="yes":
    deleted_book=input("really!!! what its\n")
    labrary.remove(deleted_book)
    print(f"naw you just have {labrary}")
print(f"dont forget to bay{wish_book}")    
    
    



