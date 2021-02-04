# from http://www.practicepython.org/  

# Ex.3 -- List Less Than 10

# Take a list, say for example this one:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# and write a program that prints out all the elements of the list that are less than 5.

#Extras:

 #  Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
 #  Write this in one line of Python.
 # Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


numero = int(input("Think of a number: "))


for num in a:
    if num < numero:
        print(num)

# Completed on 04/02/2021 with option of asking user for a number  

