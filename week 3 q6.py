#here the function is being defined. A is the placeholder for the word to be flipped. 
def FlippingWord(A):
#B is the variable of how long the word is
    B = len(A)
    S = ''
# this loop basically takes away each letter from the word and basically inverts it so everyword is backwards. 
    while B > 0:
        B -= 1
        S += A[B]
    return S
#the function is called again 
print (FlippingWord('Coding is getting so boring'))
