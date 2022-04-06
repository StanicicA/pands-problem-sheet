#Write a program that outputs whether or not today is a weekday
#Resource:https://www.delftstack.com/howto/python/python-datetime-day-of-week/#:~:text=of%20the%20day.-,Use%20the%20weekday()%20Method%20to%20Get%20the%20Name%20of,0%20and%20Sunday%20is%206. 
#Author: Andrea Stanicic

from datetime import datetime

x = datetime(2022,4,6)
if x.weekday() > 4:
    print ("It is the weekend, yay!")
else:
        print ('Yes, unfortunately today is a weekday.')

