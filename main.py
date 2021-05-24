import pyautogui as pa
import time
import sys


WAIT_TIME=30

n=len(sys.argv)
if(n>1):
    try:
       WAIT_TIME=int(sys.argv[1]) 
    except:
        print("Invalid Argument!")

     
print("Setting wait time to "+str(WAIT_TIME)+" seconds")

time.sleep(WAIT_TIME)

def scroll_slowly(amount):
    for i in range(10):
        pa.scroll(amount/10)
        time.sleep(0.1)
    time.sleep(1)
    for i in range(10):
        pa.scroll((-1*amount)/10)
        time.sleep(0.1)

while(1):
    scroll_slowly(20)
    time.sleep(WAIT_TIME)



