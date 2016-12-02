#Here a defining function has been created (one for testing prime numbers in this instance).
#N = the number to be tested.
def PrimeNumberTesting(N, division = None):
# This is the recursive test to find out if the number is prime.
    if division is None:
# Here is giving division a value which is N (number given) - 1
        division = N - 1
#division is also then greater then or equal 2
    while division >= 2:
#% here is N dividing by the division and return the remainder and if equal to 0 return false 
        if N % division == 0:
            print ('InCorrect! This number unfortunatly is not a prime number.')
            return False
        else:
            return PrimeNumberTesting(N, division-1)
    else:
        print ('Correct!This number is in fact a prime number!.')
        return True 
#here the function has been recalled and then a number has been put in that is wanted to be tested if it is prime
PrimeNumberTesting(41)
