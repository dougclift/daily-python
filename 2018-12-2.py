#Python Practice - 12-2-2018
#Exercises from practicepython.org
#Character Input
#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year 
#that they will turn 100 years old.

import datetime

name = input("What is your name? ")
age = input("What is your age? ")
year = (100 - int(age)) + datetime.date.today().year
message = "Hi, {}, you will turn 100 in the year {}".format(name, year)

print(message)