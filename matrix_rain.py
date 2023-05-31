"""
Matrix rain: a matrix rain effect in Python, by viss3

Rain can be customized by changing the following constants:
    - LIST_VALUES, the list from which the displayed characters will be taken randomly
    - COLOR, ANSI escape sequence fot colorize output in terminal
    - TOT_COLUMNS, number of characters in width
    - TOT_ROWS, number of lines
    - TIME_DELAY, seconds of delay between each iteration (decrease value for faster speed and vice versa)
    - DENSITY, 0 to 1 percentage probability of the number of characters spawned in a line (increase for heavier rain and vice versa)
"""

import random
import string
import time

# Customizable constants
LIST_VALUES = string.ascii_lowercase  # only iterable sequences
COLOR = "\033[32m"  # green (only ANSI color escape sequences)

TOT_COLUMNS = 120
TOT_ROWS = 29

TIME_DELAY = 0.07 # decrease for higher speed (in seconds)
DENSITY = 0.03  # in a range between 0 and 1


def matrix_rain():
    rain_list = []

    while True:
        # Cleaning up the console at the start of each iteration
        print("\033c", end="")

        # Remove the last line
        if len(rain_list) == TOT_ROWS:
            del rain_list[-1]
        
        # Change each character randomly at each interaction
        for line in rain_list:
            for n, item in enumerate(line):
                if item != " ":
                    letter = random.choice(LIST_VALUES)
                    line[n] = letter

        # Randomly generate a new line
        line_list = []
        for line in range(TOT_COLUMNS):
            probability = DENSITY
            random_number = random.random()
            if random_number <= probability:
                letter = random.choice(LIST_VALUES)
                line_list.append(letter)
            else:
                line_list.append(" ")
        rain_list.insert(0, line_list)

        # Print the result
        for line in rain_list:
            print(COLOR + "".join(line))

        # Wait before another interaction
        time.sleep(TIME_DELAY)


matrix_rain()
