import time, sys

maxIndent = 30 # Max spaces to indent
minIndent = 0
indent = minIndent # How many spaces to indent
indentDelta = 1 # How much it increases
line = '***********'

try:
    while True:
        print('%s%s' % (' ' * indent, line))
        time.sleep(0.1) # Pause for 1/10 of a second
        
        # add or subtract indentation
        indent += indentDelta
        
        # reset indentation direction
        if indent == maxIndent or indent == minIndent:
            indentDelta *= -1
except KeyboardInterrupt:
    sys.exit()

