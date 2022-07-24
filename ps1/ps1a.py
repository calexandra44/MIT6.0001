#!/usr/bin/env python3
# -*- coding: utf-8 -*-

annual_salary = float(input("Enter your annual salary (before tax): "))
portion_saved = float(input("Enter your annual savings percentage (in decimal format): "))
total_cost = float(input("Enter the cost of your dream home: "))
                   
r = 0.04
monthly_rate = 1 + (r)/12 #1.003
monthly_salary = int(annual_salary)/12 #10000
monthly_savings = int(monthly_salary) * float(portion_saved) #1000
portion_down_payment = float(total_cost) * .25

months = 0
current_savings = 0
for i in range(int(current_savings),int(portion_down_payment)):
   current_savings += int(monthly_savings)
   current_savings *= (monthly_rate)
   months += 1
   if float(current_savings) >= float(portion_down_payment):
         break
print ("The number of months it will take to save for a down payment for your dream home is:" )
print(months)

          #  else float(current_savings) < float(total_cost):
            #float(current_savings) += float(monthly_savings)

#n1 = (float(first_monthly_earnings) + float(monthly_savings)) * float(monthly_rate)
#n2 = (float(n1) + float(monthly_savings)) * float(monthly_rate)

#saving this for part 2 : portion_down_payment = float(annual_salary)*.25
