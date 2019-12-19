import time
from grovepi import *
import random
import requests

LEDBAR = 5
USR = 4
URL = 'https://hiq9swtkie.execute-api.eu-west-1.amazonaws.com/dev/warningMessage'

pinMode(LEDBAR, "OUTPUT")

while True:
    try:

        ledBar_init(LEDBAR, 1)
        time.sleep(.5)

        distance = lambda d : round((((500 - (d if d <= 500 else 500)) / 500)*100)/10)

        bar_level = distance(ultrasonicRead(USR))
        ledBar_setLevel(LEDBAR, bar_level)
        time.sleep(1)

        msg = {'score': bar_level*10}

        if bar_level >= 8:
            send_msg = requests.post(URL, json=msg)

    except KeyboardInterrupt:
        ledBar_setBits(LEDBAR, 0)
        break
    except IOError:
        print("ERROR")
