#program that asks the user to input any positive integer 
#and outputs the successive values of the following calculation
#the next value by taking the current value and, 
#if it is even, divide it by two, but if it is odd, multiply it by three and add one
#Resource: https://codereview.stackexchange.com/questions/245607/check-if-number-is-divisible-by-three-and-two
# Author: Andrea Stanicic

n = int(input('Please enter a positive integer:'))
print (n)

if (n % 2 == 0):
     print (n // 2)
elif (n % 3 == 0):
      print(n * 3 + 1)
      n = n-1
    
     
