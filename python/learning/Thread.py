# thread = a flow of execution. Like a separate order of instructions.
#               However each thread takes a turn running to achieve concurrency
#               GIL = (global interpreter lock),
#               allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound =   program/task spends most of its time waiting for internal event (CPU intensive)
#               use multiprocessing

# io bound =    program/task spends most of its time waiting for external events(user input, web scraping)
#               use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print('You finished eating breakfast')
def drink_coffee():
    time.sleep(4)
    print('You finished drinking coffee')
def study():
    time.sleep(5)
    print('You finished studying')

x = threading.Thread(target=eat_breakfast, args=()) # You need to write the function without ()
x.start()

y = threading.Thread(target=drink_coffee, args=()) # You need to write the function without ()
y.start()

z = threading.Thread(target=study, args=()) # You need to write the function without ()
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())