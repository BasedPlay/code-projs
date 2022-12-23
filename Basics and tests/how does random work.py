import random

# Generate a random float between 0 and 1
x = random.random()
print(x)

# Generate a random float between 1 and 10
y = random.uniform(1, 10)
print(y)

# Generate a random integer between 1 and 10
z = random.randint(1, 10)
print(z)

# Generate a random element from a list
list = [1, 2, 3, 4, 5]
random.shuffle(list)
print(list)

# using random.choice you can select a random value from a variable list of values
# in a bracket separated by commas

w = random.choice(list)

print(w)

names = ['joe', 'Noah',]
abc = random.choice(names)

print(abc)

