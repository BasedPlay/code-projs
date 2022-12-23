i = 1
while i <= 5:
    print(i)
    i = i+1
print ('done!')

# guessing game

import random

secret_num = 9

guesses = 0
guess_limit = 3

while guesses + guess_limit:
    guess = int(input('Guess a number 1-10: \n'))
    guesses += 1
    if guess == secret_num:
        print('You Win!')
        break
    if (guess != secret_num) and (guesses < 3):
        print('Try again!')
else:
    print('You Lose!')