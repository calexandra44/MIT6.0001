#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#1. Asks the user to enter a number “x” 
#2. Asks the user to enter a number “y”
#3. Prints out number “x”, raised to the power “y”. 
#4. Prints out the log (base 2) of “x”.

import numpy as nm

x = input("Enter a value for 'x': ")
y = input("Enter a value for 'y': ")
print(int(x)**(int)(y))
print(nm.log(int((x))))
      
