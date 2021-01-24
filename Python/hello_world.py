print('Starting up!!!')

d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)


name = input("Please enter your name: ")
print("My name is " + name)

age = int(input("Please enter your age: "))
print('Thank you.')

oldage = str(100 - age)
year = (str((2021-age)+100))\n
print("Hi " +name+" , You will turn 100 years old in "+ oldage + " years, i.e. in " + year)