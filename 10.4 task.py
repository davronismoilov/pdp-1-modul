from datetime import datetime
from time import sleep

while True:
    try:

        now = datetime.now()
        print(now.strftime("%X"))
        sleep(2)
    except BaseException as e:
        print(e)
        break
