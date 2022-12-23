name = input('What is your name? \n')
print('Hello, ' + name)

color = input('What is your favorite color? \n')

print(name + ' likes the color ' + color)

birth_year = input('Birth Year: ')

import datetime

now = datetime.datetime.now()
year = now.year
age = year - int(birth_year)

# here str() is used to turn the integer value of variable age into a string
# which can then be concatenated ( + ) with the other strings. 
# Use this to change values from string/interger/float/boolean to another class

print('You are ' + str(age) + ' years old.')

weight = input('What is your weight in lbs? \n')

weight_kgs = int(weight) * 0.453592

# However, here, rather than turning th float value of weight_kgs into a string in order to add
# them to the other strings we simple use wiggly brackets to call in whatever the value of weight Kgs 
# is withing a single set of quotes, all you have to do is add f (stands for format) 
# before the quotes but inside the ()

print(f'You weigh {weight_kgs} kilograms')



weight = input('how much do you weigh? \n')

k_or_l = input("(K)gs or (L)bs? \n")

if k_or_l.upper() == 'K':
    convertion = (int(weight)*2.20462)
    k_or_l = 'Kgs'

else:
    convertion = (int(weight)/2.20462)
    k_or_l = 'lbs'

print(f'You weigh {convertion} {k_or_l}')