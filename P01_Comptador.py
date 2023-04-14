# Imports go at the top
from microbit import *

counter = 0
# Code in a 'while True:' loop repeats forever

while True:
    display.scroll(counter)    


    if button_a.is_pressed():  # change is for was
        counter = counter + 1  # "is" checks if the button IS CURRENTLY being pressed
                               # "was" checks if the button WAS PRESSED or not
    if button_b.is_pressed():
        counter = counter - 1
    
    if button_a.is_pressed() and button_b.is_pressed():
        counter = 0
        
    