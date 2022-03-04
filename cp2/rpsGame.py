import random, sys, re

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.

wins = 0
losses = 0
ties = 0

moveNames = { 'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS' }
moveCodes = { 1: 'r', 2: 'p', 3: 's' }

def moveName(move):
    return moveNames.get(move, 'ROCK')

def moveCode(number):
    return moveCodes.get(number, 'r')
    
def isValidMove(move):
    return move in moveNames.keys()

def win():
    global wins
    print('You win!')
    wins += 1

def lose():
    global losses
    print('You lose!')
    losses += 1

def tie():
    global ties
    print('Its a tie!')
    ties += 1

def checkMoves(playerMove='r', computerMove='r'):
    playerWins = ['rs', 'pr', 'sp']

    if playerMove+computerMove in playerWins:
        win()
    elif playerMove == computerMove:
        tie()
    else:
        lose()

while True: # The main game loop
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')

    valid = False
    while not valid: # The player input loop
        print('\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program
        
        valid = isValidMove(playerMove)
        if not valid:
            print('ERROR: Type one of r, p, s, or q.')

    #Display what the player chose:
    print(f'P: {moveName(playerMove)}')
    print('versus...')

    # Display what the computer chose:
    computerMove = moveCode(random.randint(1, 3))
    print(f'C: {moveName(computerMove)}')

    # Display and record the win/loss/tie:
    checkMoves(playerMove, computerMove)

