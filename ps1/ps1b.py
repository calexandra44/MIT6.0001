#!/usr/bin/env python3
# -*- coding: utf-8 -*-

annual_salary = float(input("Enter your annual salary (before tax): "))
portion_saved = float(input("Enter your annual savings percentage (in decimal format): "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual raise (in decimal format): "))
                   
r = 0.04
monthly_rate = 1 + (r)/12 
monthly_salary = int(annual_salary)/12
monthly_savings = int(monthly_salary) * float(portion_saved)
portion_down_payment = float(total_cost) * .25
salary_with_raise = (1 + semi_annual_raise) * annual_salary #1.2x 120000 = 144000
monthly_raise = (1+ semi_annual_raise)/12 #1.2/12
monthly_salary_w_raise = (salary_with_raise/12) #14400/12

#months = 0
#current_savings = 0
#for i in range(int(current_savings),int(portion_down_payment)):
 #  current_savings += int(monthly_savings)
  # current_savings *= (monthly_rate)
  # months += 1
   #for i in range(0,6)
          # monthly_savings == monthly_salary_w_raise
   #if float(current_savings) >= float(portion_down_payment):
    #     break
#print ("The number of months it will take to save for a down payment for your dream home is:" )
#print(months)

# range = start stop step
# for i in range(0, 6, months)
    # monthly_raise 
