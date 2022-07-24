#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#1. Asks the user to enter a number “x” 
#2. Asks the user to enter a number “y”
#3. Prints out number “x”, raised to the power “y”. 
#4. Prints out the log (base 2) of “x”

#1 and 2
x = input("Enter a value for x: ")
y = input("Enter a value for y: ")

# trying to print out variables as integers or at the very least as a string
# star date.september 18 1996 i did it BABY HEELP ME THANK U 

print(x+y)
print(int(x)+int(y))

#3
print(int(x)**(int(y)))

#4
import numpy as np
print((np.log(int(x))))




