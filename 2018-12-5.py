#Python Practice - 12-2-2018
#Exercises from practicepython.org
#Divisors
#Create a program that asks the user for a number and then prints out
#a list of all the divisors of that number. (If you don’t know what 
#a divisor is, it is a number that divides evenly into another number. 
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

number = input("Give me a number: ")

x = range(1, int(number))
y = []

for num in x:
	if int(number) % num == 0:
		y.append(num)
				
#print out list of the divisors			
print(*y,sep=", ")
		

