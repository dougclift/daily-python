#Python Practice - 12-2-2018
#Exercises from practicepython.org
#LIST LESS THAN TEN
#Take a list and write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for item in a:
	if item < 5:
		print(item)
		
#Instead of printing the elements one by one, make a new list that has 
#all the elements less than 5 from this list in it and print out this new list.

b = []

for item in a:
	if item < 5:
		b.append(item)
		
print(b)

#Ask the user for a number and return a list that contains only elements from the 
#original list a that are smaller than that number given by the user.

number = input("Give me a number: ")

c = []
for item in a:
	if item < int(number):
		c.append(item)
		
print(c)