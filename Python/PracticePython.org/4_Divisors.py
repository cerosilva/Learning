# from http://www.practicepython.org/  

# Ex. 4 -- Divisors
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

print('Starting up!!!')


num = int(input("Think of a number: "))

listRange = list(range(1,num+600))

divisorlist = []

for number in listRange:
    if num % number == 0:
        divisorlist.append(number)

print(divisorlist)

# Completed on 05/02/2021

#TO REMEMBER

# % is modulo which gives you the remainder of the division. 