#!/usr/bin/python
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time() # get first lap's start time
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %ss (%ss)' % (lapNum, totalTime, lapTime), end='')
        lapNum+=1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    print('\nDone.')
