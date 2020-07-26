# More try catch demos

import time
import sys


indent = 0   # How many spaces to indent
indentIncreasing = True  # Controls whether the indent is increasing or not

try:
    while True:  # Main Loop
        print(" " * indent, end='')
        print("********")
        time.sleep(0.05)  # Pause for 0.1s

        if indentIncreasing:
            #  Increase the number of spaces
            indent += 1
            if indent == 20:
                # Change Direction
                indentIncreasing = False
        else:
            #  Decrease the number of spaces
            indent -= 1
            if indent == 0:
                # Change Direction
                indentIncreasing = True


except KeyboardInterrupt:
    sys.exit()

