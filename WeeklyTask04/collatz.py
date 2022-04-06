#program that asks the user to input any positive integer 
#and outputs the successive values of the following calculation
#the next value by taking the current value and, 
#if it is even, divide it by two, but if it is odd, multiply it by three and add one
#Resource:https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff & https://codereview.stackexchange.com/questions/245607/check-if-number-is-divisible-by-three-and-two
# Author: Andrea Stanicic

number=int(input('Please enter a positive integer:'))

def collatz(number):

    while number !=1:
        if number% 2 == 0:
            number= number//2
            print(number)

        else:
           number=  3 * number + 1
           print(number)    


collatz(number)