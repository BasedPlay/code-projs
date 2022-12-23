# within the same print() text, you can use \n to create a new line of text; i.e. pressing enter
# You can also use \t to indent the text; i.e. pressing TAB. you can use this in conjunction and multiple times

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")
print('this text is not indented')
print('\tthis text indented once')
print('\t\tthis text is indented twice. \nthis is basically pressing enter')

# You can define variables as text and then call the variable inside a print text by using 
# f before the quotes and then using {variable name} the f stands for format
# to insert the variable in said spot

first_name = "Douglas"
last_name = 'Douglas'
age = "32"

print (f'\nhello, I am {first_name} {last_name}, I am {age} years old')

# furthermore, you can usen list variables, as well as the random module to pick at random 
# please see 'how does random work.py' for examples and explanation

import random 

first_names = ['Joe', 'Noe', 'Ash']
last_names = ['Biden', 'Cazares', 'Ketchum']
ages = ['80', '18', '25']

a = random.choice(first_names)
b = random.choice(last_names)
c = random.choice(ages)

print(f"howdy, I am {a} {b}, I am {c} years old")

set = random.randint(1, 3)  # fix: remove third argument and change range to 1 to 3 (inclusive)

info_1 = ''  # fix: define variables as strings instead of lists
info_2 = ''
info_3 = ''

if set == 1:
    info1 = 'Joe'
    info2 = 'biden'
    info3 = '79'
elif set == 2:  # fix: use elif instead of if
    info1 = 'Noe'
    info2 = 'Cazares'
    info3 = '18'
elif set == 3:  # fix: use elif instead of if
    info1 = 'Ash'
    info2 = 'Ketchum'
    info3 = '25'

print(f"hey, I am {info1} {info2}, I am {info3} years old")  # fix: access elements of lists using index notation

# the triple quote """ allows for multiple line to be part of the statement ( USEFUL FOR ASCII)

ascii_art = """ 
TTTTTTTTTTTTTTTTTTTTTTTEEEEEEEEEEEEEEEEEEEEEE   SSSSSSSSSSSSSSS TTTTTTTTTTTTTTTTTTTTTTT
T:::::::::::::::::::::TE::::::::::::::::::::E SS:::::::::::::::ST:::::::::::::::::::::T
T:::::::::::::::::::::TE::::::::::::::::::::ES:::::SSSSSS::::::ST:::::::::::::::::::::T
T:::::TT:::::::TT:::::TEE::::::EEEEEEEEE::::ES:::::S     SSSSSSST:::::TT:::::::TT:::::T
TTTTTT  T:::::T  TTTTTT  E:::::E       EEEEEES:::::S            TTTTTT  T:::::T  TTTTTT
        T:::::T          E:::::E             S:::::S                    T:::::T        
        T:::::T          E::::::EEEEEEEEEE    S::::SSSS                 T:::::T        
        T:::::T          E:::::::::::::::E     SS::::::SSSSS            T:::::T        
        T:::::T          E:::::::::::::::E       SSS::::::::SS          T:::::T        
        T:::::T          E::::::EEEEEEEEEE          SSSSSS::::S         T:::::T        
        T:::::T          E:::::E                         S:::::S        T:::::T        
        T:::::T          E:::::E       EEEEEE            S:::::S        T:::::T        
      TT:::::::TT      EE::::::EEEEEEEE:::::ESSSSSSS     S:::::S      TT:::::::TT      
      T:::::::::T      E::::::::::::::::::::ES::::::SSSSSS:::::S      T:::::::::T      
      T:::::::::T      E::::::::::::::::::::ES:::::::::::::::SS       T:::::::::T      
      TTTTTTTTTTT      EEEEEEEEEEEEEEEEEEEEEE SSSSSSSSSSSSSSS         TTTTTTTTTTT      """

print (ascii_art)