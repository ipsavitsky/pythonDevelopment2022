import time
from pyfiglet import Figlet

def figdate(font='graceful', format='%Y %d %b %A'):
    time_str = time.strftime(format)
    return Figlet(font).renderText(time_str)
