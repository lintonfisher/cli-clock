import datetime
import os
import time

from pyfiglet import figlet_format

while True:
    os.system('clear')

    h = str(datetime.datetime.now().strftime('%H'))
    m = str(datetime.datetime.now().strftime('%M'))
    s = str(datetime.datetime.now().strftime('%S'))

    time_string = '%s:%s:%s' % (h, m, s)
    figlet = figlet_format(time_string, font='3x5')
    replace_with_char = figlet.replace('#', "\u2588")

    print(replace_with_char)

    time.sleep(1)
