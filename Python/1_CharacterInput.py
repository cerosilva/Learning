# from http://www.practicepython.org/  

print('Starting up!!!')

# Ex.1 -- Character Input

# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

name = input("Please enter your name: ")
print("My name is " + name)

age = int(input("Please enter your age: "))
print('Thank you.')

oldage = str(100 - age)
year = (str((2021-age)+100))
stmt = ("Hi " +name+" , You will turn 100 years old in "+ oldage + " years, i.e. in " + year)
print(stmt)

repeat = input("Would you like me to say that again?:  ")

repeattimes = int(input("How many times?: "))
    
print(stmt * repeattimes)

print('Have a nice day!')

# Finished on 24/01/2021

# Ex.2 -- Odd Or Even

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?
# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

#Comment to test new branch