#calculating Body Mass Index
#Resource: https://www.w3resource.com/python-exercises/python-basic-exercise-66.php
#Author:Andrea Stanicic

height = float (input("Enter weight(kg):"))
weight = float (input("Enter height(cm):"))

print ("The BMI is (kg/m2):",round(weight / (height * height),2))

