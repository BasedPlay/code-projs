# within the same print() text, you can use \n to create a new line of text; i.e. pressing enter
# You can also use \t to indent the text; i.e. pressing TAB. you can use this in conjunction and multiple times

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")
print('this text is not indented')
print('\tthis text indented once')
print('\t\tthis text is indented twice. \nthis is basically pressing enter')

# You can define variables as text and then call the variable inside a print text by using 
# f before the quotes and then using {variable name} to insert the variable in said spot

firstname = "Douglas"
lastname = 'Douglas'
age = "32"

print (f'hello I am {firstname} {lastname}, I am {age} years old')

# furthermore, you can usen list variables, as well as the random module to pick at random 
# please see 'how does random work.py' for examples and explanation

import random 

firstnames = ['Joe', 'Noe', 'Ash']
lastnames = ['Biden', 'Cazares', 'Ketchum']
ages = ['80', '18', '25']

a = random.choice(firstnames)
b = random.choice(lastnames)
c = random.choice(ages)

print(f"hello I am {a} {b}, I am {c} years old")

set = random.randint(1, 2, 3)

info1 = ['']
info2 = ['']
info3 = ['']

if set == 1:
    info1 = ['Joe']
    info2 = ['biden']
    info3 = ['79']

if set == 2:
    info1 = ['Noe']
    info2 = ['Cazares']
    info3 = ['18']

if set == 3:
    info1 = ['Ash']
    info2 = ['Ketchum']
    info3 = ['25']


print(f"hello I am {info1} {info2}, I am {info3} years old") 