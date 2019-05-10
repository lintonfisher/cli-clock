import datetime
import os
import time

try:
    from pyfiglet import figlet_format
except ImportError:
    print('Error, module pyfiglet is required. Run: sudo pip3 install pyfiglet')

# VARIABLES
padding             = [1, 0, 0, 3]
font_name           = '3x5'
custom_char_replace = {
                        '#': '@',
                        '@': '\u2588'
                      }
time_format         = '%H:%M:%S'
update_frequency    = 1

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

    # Apply padding
    # Top padding
    for i in range(padding[0]):
        print()

    # Right padding (useless until text alignment added)
    # Bottom padding (pretty much useless as well)
    # Left padding
    for i in range(padding[3]):
        figlet_string.replace('\n', '\n ')

    # Print the string
    print(figlet_string)

    # Sleep
    time.sleep(update_frequency)
