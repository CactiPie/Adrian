Why hello there

import random
num = random.randint(1, 25)
guesss = 0
while True:
  print('guess a number between 1 and 25:')
  guess = int(input())
  if guess > num:
    print('Guess lower.')
  elif num > guess:
    print('Guess higher.')
  else:
    break
print('You got it! it was', num)
