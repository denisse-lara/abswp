
def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

try:
    print('Enter number:')
    number = int(input())
    
    while number != 1:
        number = collatz(number)
        print(number)
except ValueError:
    print('ERROR: input is not a number')

