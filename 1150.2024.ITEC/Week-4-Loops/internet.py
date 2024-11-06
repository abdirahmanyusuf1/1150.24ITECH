from urllib import request
from time import sleep
import os
url = 'https://www.google.com'
seconds_to_sleep_between_checks = 3



while True:
    print('checking if online.....')
    try:

        request.urlopen(url).read()
        print('You are probably online!')
        os.system('say hey, you are online!')
    except:
        print('You are not online')
        os.system('say hey, you are not online!')
    print(f'Sleeping for {seconds_to_sleep_between_checks} seconds')
    print()
    sleep(seconds_to_sleep_between_checks)

