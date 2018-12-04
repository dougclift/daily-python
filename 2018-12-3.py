#Python Practice - 12-2-2018
#Exercises from practicepython.org
#ODD OR EVEN
#Ask the user for a number. Depending on whether the number is even or odd, 
#print out an appropriate message to the user.

number = input("Please enter a number: ")

if int(number) % 2:
	print(str(number) + " is odd")
else:
	print(str(number) + " is even")