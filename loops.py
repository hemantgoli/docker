#!/bin/python

import time, os

print('''
    Welcome to Python !!
    (:
      ''')

################################################################################ Height Check
try:
    height = int(input("Please enter your height in CM : "))

    if (height >= 120):
        print("Proceed to next !\n")
    elif (height >= 100):
        print("you are not allowed for kids only !!\n")
    else:
        print ("you are not allowed ! \n")

except: print("Number only\n")

################################################################################ odd or even

number = int(input("Enter your number to check odd / even : "))
if (number%2 == 0):
    print("Numebr is even !\n")
else:
    print("number is odd !\n")

################################################################################ Leap year or not

leap_year = int(input("Enter the year : "))

if(leap_year%4 == 0 and leap_year%400 == 0 and (leap_year%100)%2 == 0):
    print ("this is leap year")
else:
    print("This is not leap year")

############################################################################### multi if loops if true

try:
    age = int(input("Enter your age : "))
    
    if(age >= 18):
        print ("your are eligble !")
        ticket = 18
        photo = input("Do you want photo ? yes/no ")
        if (photo == "yes"):
            photo_bill = 3
            total_bill = ticket + photo_bill 
            print("Your total bill = " +str(total_bill))
        else: print("Your total bill = ", ticket)
except: print("Enter proper value")

############################################################################ Love Calculator
try:
    girl = (str(input("Enter Girl Name : "))).lower()
    boy = (str(input("Enter Boy Name : "))).lower()

    l = girl.count("l")
    o = girl.count("o")
    v = girl.count("v")
    e = girl.count("e")

    print("Your score is : ", l+o+v+e )
except:
    print("Enter proper value !!")

###########################################################################  Time count
time_count = int(input("Enter your count time in sec :"))
os.system('cls')

while(time_count != 0):
    time_count=time_count-1
    time.sleep(2)
    os.system('cls')
    if(time_count == 0):
        print(" GO ")
        #os.system('shutdown /r')
    else: 
        print("Counting time : ",time_count)

############################################################################  
        



    










