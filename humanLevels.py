# A python script for moving function increases to a logarithmic scale

# Python imports
import numpy as np
import os
import sys

# Necessary installs
# xbacklight
# pamixer


# Defines the function for altering the backlight
def human_levels(
        get_fn="xbacklight -get", 
        set_fn="xbacklight -set ",
        inc=True,
        max_value=100,
        increment=0.2
        ):

    # Gets the current backlight level
    current_level = os.popen(get_fn).read().splitlines()[0]
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
    os.system(set_fn+str(new_level))


## Main function

if __name__ == '__main__':

    if int(sys.argv[1]) == 0:

        human_levels(inc=int(sys.argv[2]))

    elif int(sys.argv[1]) == 1:

        human_levels(
                inc=int(sys.argv[2]),
                get_fn="pamixer --get-volume",
                set_fn="pamixer --allow-boost --set-volume ",
                max_value=200,
                increment=0.1
                )

