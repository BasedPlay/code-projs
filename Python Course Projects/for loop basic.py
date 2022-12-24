#for loops are useful for listing or repeating actions a certain number of times, when using for loops
#with strings, a value will be assinged to the variable, itc 'item' for every character of the string
#the value will be string in question so line 5 will print 'w' then 'o' and so on until it finished the word

for item in ("word"):
    print (item)

#for loops with lists of strings or numbers behave similar to a string but rather,
# will attach the string/number value to the variable and it will therefore print each item in the list
#i.e. line 12 will print 'do' then 're' etc.. and line 14 will print '1' then '2' etc..

for item in ['do', 're', 'mi', 'fa', 'sol', 'la', 'ti', 'do']:
    print (item)
for item in [1,2,3,4,5]:
    print (item)

#The range function in Python is a built-in function that returns a sequence of numbers, 
# starting from 0 by default, and increments by 1 (also by default), and ends at a specified number.
for item in range(10): #prints numbers from 0-9
    print(item)

#start and step are optional parameters. start specifies the starting number for the sequence,
# and step specifies the number to increment by.

for item in range(5,10): #prints numbers from 5-9
    print(item)    

for item in range (0,10,2): #prints numbers from 0-9 in increments of 2
    print (item)

#It's important to note that the range function generates a sequence of numbers,
#but it does not create a list. To create a list from the sequence of numbers generated
#by the range function, you can use the list constructor. For example:

item = list(range(10))
print(item)

# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#PRICE CALCULATOR

prices = [10,20,30]
total = 0
for price in prices:
    total += price
print (f'Total: ${total}')

#COORDINATE GENERATOR

for x in range(4):
    for y in range(4):
        print (f'({x}, {y})')

#PRINT F of X's

list = [5,2,5,2,2]
num_x = 0

for layer in list:
    num_x=layer
    print("x"*num_x)

print('\n')

list = [2,2,2,2,5]
num_x = 0

for layer in list:
    f = ''
    for count in range(layer):
        f += 'x'
    print (f)

print ('im scared')