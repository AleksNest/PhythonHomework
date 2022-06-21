from datetime import datetime as dt
from time import time

def logger(data, str):
    time  = dt.now().strftime('%H:%M')           
    with open('logger.csv', 'a+', encoding='utf-8' ) as file:
        file.write('{} -  {}: {};  \n'.format(time, str, data))

