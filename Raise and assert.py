import logging

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbol needs to be a string of length 1')
    if (width<2) or (height<2):
        raise Exception('"width" and height must be at least 2')
    print(symbol * width)
    for i in range(height-2):
        print(symbol + (' ' * (width-2)) + symbol)
    print(symbol * width)
    print(boxPrint('*', 15, 5))#this worked on idle but not here

import traceback
try:
    raise Exception('This is an error message')
except:
    errorFile = open('error_log.txt', 'a')


logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %messages)s')
print(1*2*3*4)
print(7*6*5*4*3*2*1)