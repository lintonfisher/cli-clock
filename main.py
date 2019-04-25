import datetime
import os
import time

from pyfiglet import figlet_format

# VARIABLES

# Padding
top_padding_amount      = 0
right_padding_amount    = 0
bottom_padding_amount   = 0
left_padding_amount     = 0

# Font
font_name = '3x5' # (for list of fonts see: http://www.figlet.org/fontdb.cgi)
custom_char_replace = {'#': '\u2588'} # Specify characters to replace

# Time (for formatting options see: http://strftime.org/)
time_format = '%H:%M:%S'

while True:
    # Clear the screen to make the clock appear 'in-place'
    os.system('clear')

    # Convert the current time to the defined format
    time_string = datetime.datetime.now().strftime(time_format)
 
    # Turn the string into a figlet ASCII art string
    figlet_string = figlet_format(time_string, font=font_name)

    # Replace any characters
    for char in custom_char_replace:
        figlet_string = figlet_string.replace(char, custom_char_replace[char])

    # Print the string
    print(figlet_string)

    # Sleep
    time.sleep(1)
