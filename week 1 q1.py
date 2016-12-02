#here is the original array that i actually want to go ahead and shuffle.
MyArray=[1,2,3,4,5]
#here i have changed the orders of the array that will in turn change the order of the orignial array.
#here i have done two change orders to just show tqo shuffles resulting in two different results.
ChangetheOrder=[1,0,3,1,2]
#the arrayshere show each space the numbers can move from 0 (at the begining) to 4 (the ending).
ChangetheOrder1=[3,4,0,1,2]
#to shuffle the array it is put down here again and then used within in a loop.
MyArray = [MyArray[i] for i in ChangetheOrder]
#this changes the order. Shuffles it
MyArray2 = [MyArray[i] for i in ChangetheOrder1]

print (MyArray, MyArray2)
