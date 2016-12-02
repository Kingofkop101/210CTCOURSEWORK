# Here I have created a defining a function (for the perfect square). a represents a placeholder for a number.
def perfsq(a):
# y is equal to the perfsq
    y = a
#using a true and if statement loop to figure out the perfect square of number
    while True:
        if y**2 <= a:
            # the result will be shown on another window screen
            #%s is used in order to insert the intergers one for the number and other for highest perfect square
            print ("The biggest perfect square of %s or less then that is going to be %s" %(a,y**2))

            return y**2 #value is returned sin order for it to be used not within thefunction but out 
        else:
            y -= 1

#by using this you will be able to add your own number in so that the highest square for that number and less can be found
testnumb = 90
biggestsqr = perfsq(testnumb)

