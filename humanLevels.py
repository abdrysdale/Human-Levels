# A python script for moving function increases to a logarithmic scale

# Python imports
import numpy as np
import os
import sys

# Necessary installs
# xbacklight


# Defines the function for altering the backlight
def backlight(inc=True):

    # Defines constants
    max_value = 100
    increment = 0.1

    # Gets the current backlight level
    current_level = os.popen('xbacklight -get').read().splitlines()[0]
    current_level = float(current_level)
    

    # Increases the backlight
    if inc == True:

        # Obtains the new level via the formula:
        # y_n+1 = A exp( ln(y_n/A) + c
        new_level = int(max_value*np.exp( np.log(current_level/max_value) + increment))

        # Forced change of new_level for small values
        if np.abs(new_level - current_level) < 0.5:

            new_level += 1

    # Decreases the backlight
    else:

        new_level = int(max_value*np.exp( np.log(current_level/max_value) - increment))

    print(current_level, new_level)
    # Sets the level
    os.system('xbacklight -set '+str(new_level))


## Main function

if __name__ == '__main__':

    if int(sys.argv[1]) == 0:

        backlight(inc=int(sys.argv[2]))

