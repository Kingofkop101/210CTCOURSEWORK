def LOOKINGUP(array,L,UP,LOWEST, HIGHEST):
#false is returned if the interval is not found
    while HIGHEST-LOWEST <=1:
        return "this is:",False
    
    M= (HIGHEST + LOWEST)//2

    if array[M]>=L and array [M]<= UP:
            return True

    else:
        
        if UP <=array[M]:
            return LOOKINGUP(array, L, HIGHEST-1,UP, LOWEST)
        
        elif L >= array[M]:
            return LOOKINGUP(array, L,HIGHEST, UP,LOWEST+1)

#hereis where the low is inputted
LOWEST=10
#here is where the list is inpiuted
LISTS=[2,3,7,8,13]
#the high is calculated by the length of list
HIGHEST=len(LISTS)

print (LOOKINGUP(LISTS,0,2,LOWEST,HIGHEST))       
print ("here is the list thats being inputted:~", LISTS)
