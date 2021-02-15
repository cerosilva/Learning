# from http://www.practicepython.org/  

# Ex. 6 -- String Lists

# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

firststring = str(input("Think of a string: "))

print(firststring)

reverse = firststring[::-1]

print(reverse)

if firststring == reverse:
    print("This is a Palindrome")
else:
    print("This is not a Palindrome")


# Completed on 15/02/2021 