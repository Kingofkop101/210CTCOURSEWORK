A = int(input("What number would you like to know a factoriall of:~"))

if A < 0:
    #THE USER NEEDS TO PUT IN A POSITIVE NUMBER OTHERWISE THIS WILL BE SHOWN
    print("The number needs to be that of a positive one")
elif A >= 0:
    #THE NUMBER PUT IN IS THEN CALCULATED TO FIND THE FACTORIAL
    Z= 1
    while A >= 1:
        Z =  Z * A
        A = A -1
    print(Z)
#THIS WILL CALCULATE THE ZEROS FOT THE FACTORIAL ANSWER AND VALUE IS AT ZERO
trailingzero = 0
#WHILE LOOP STARTS SO THAT THE ZEROS OF THE FACTORIAL CAN BE COUNTED FOR
while True:
#ZEROS ARE CHECKED IN THIS IF STATEMENT BY DIVIVING FACTORIAL BY 10S
    if Z % 10 == 0:
        trailingzero += 1
        # FOR EVERY ZER0 A 1 IS ADDED
        Z = Z / 10         
    else:
        break
print("number of trailing 0s is: ", trailingzero)




    


