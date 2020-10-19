#Using Random Number Generator

import random
 
min_value = 1
max_value = 6
 
again = True
 
while again:
    print(random.randint(min_value, max_value))
 
    another_roll = input('Want to roll the dice again? ')
 
    if another_roll == 'yes' or another_roll == 'y':
        again = True
    else:
        again = False
