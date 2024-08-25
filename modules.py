# Modules
import time

print(time.asctime())
print(time.timezone)

# importing specific method from a module
from time import asctime

print(asctime())

# another example
from time import asctime, sleep

print(asctime())
sleep(5)
print(asctime())

# all details of a module
dir(time)

# Module search path
import sys
sys.path

# Changing default python path
PYTHONPATH = path1; pathn
pwd


# Example
import sys

file_name = "C:\\Users\\deepak\\Desktop\\ENBD_AACOE\\Python_Course\\testing.txt"

try:
    with open(file_name) as test_file:
        for line in test_file:
            print(line)
            
except:
    print('Could not open {}.'.format(file_name))
    # sys.exit(1)


# User defined module
# def say_hi():
#     print('Hi')
    
import say_hi

say_hi.say_hi() 


# Example
def say_hi():
    print('Hi')

def main():
    print('Hello from say_hi.py!')
    say_hi()
    
if __name__ == '__main__':
    main()
    
dir(say_hi)

            
            
            
            
            
            
            
            
            
            
            
            
        