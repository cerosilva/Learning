# from http://www.practicepython.org/  

# Ex. 5 -- List Overlap

# Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

#Extras:
#    Randomly generate two lists to test this
#    Write this in one line of Python 

num1 = int(input("Think of a number: "))

a = list(range(3,(num1+6)*20))

print("Thanks")

num2 = int(input("Now give me another number: "))
b = list(range(1,(num2-2)*15))

print(a)
print(b)

c = [x for x in list(a) if x in list(b)]

print(c)

# Completed on 06/02/2021 using inputs to generate random lists