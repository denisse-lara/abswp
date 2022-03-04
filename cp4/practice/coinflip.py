import random

nonOverlappingNumberOfStreaks = 0
overlappingNumberOfStreaks = 0

def streaksNonOverlapping(flips):
    # count how many streaks of 6 H or T happen in the list
    # does not count overlaps, so HHHHHHH counts as 1
    strList = ''.join(flips)
    headStreaks = strList.count('H'*6)
    tailStreaks = strList.count('T'*6)
    print(f"(Non-overlapping) H streaks: {headStreaks}; T streaks: {tailStreaks}")
    return headStreaks + tailStreaks

def streaksOverlapping(flips):
    # count how many streaks of 6 H or T happen in the list
    # counts overlaps too, so HHHHHHH counts as 2
    h = 'H'*6
    t = 'T'*6
    headStreaks = sum(''.join(flips[i:]).startswith(h) for i in range(len(flips)))
    tailStreaks = sum(''.join(flips[i:]).startswith(t) for i in range(len(flips)))
    print(f"(Overlapping) H streaks: {headStreaks}; T streaks: {tailStreaks}")
    return headStreaks + tailStreaks


for n in range(10000):
    # builds a list of 100 random H and T
    flips = [random.choice(['H', 'T']) for _ in range(100)]
    print(f"{n+1} {flips}")

    nonOverlappingNumberOfStreaks += streaksNonOverlapping(flips)
    overlappingNumberOfStreaks += streaksOverlapping(flips)

print('Chance of streaks (overlapping): %s%%' % (overlappingNumberOfStreaks / 100))
print('Chance of streaks (non-overlapping): %s%%' % (nonOverlappingNumberOfStreaks / 100))
