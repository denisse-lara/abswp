import random
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format=' %(asctime)s -  %(levelname)s -  %(message)s'
)

sides = ('heads', 'tails')
guess = ''

def readGuess():
    global sides
    g = ''
    while g not in sides:
        print('Guess the coin toss! Enter heads or tails:')
        g = input()
    return g

guess = readGuess()
toss = sides[random.randint(0, 1)] # 0 is heads, 1 is tails

logging.debug("%s==%s is %s" % (toss, guess, toss == guess))
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = readGuess()

    logging.debug("%s==%s is %s" % (toss, guess, toss == guess))
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
