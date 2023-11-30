#!/bin/python

import os, time, random

print ("Welcome Python !!!!")

#fruits = ["apple", "banana", "grapes"]

fruits = "any"

for fruit in fruits:
    print(fruit)


################################################## Student average height

height = input("Enter the heights : ").split()
total = 0
for i in range(0, len(height)):
    height[i] = int(height[i])
    total += height[i]

print("Avg Height = ", int(total/len(height)))

###############################################  highest score

score = input("Enter the score with space : ").split()
for sco in range(0, len(score)):
    score[sco] = int(score[sco])

print("First max number : ", max(score))

score.remove(max(score))

print("second highest number : ", max(score))

##################################################  add numbers

num_range = int(input("Enter the max number to add from 0 : "))
total = 0
for i in range(0, num_range+1):
    total += i
print(total)

##############################################  add only even number

ev = 0

for i in range(0, num_range+1):
    if (i%2==0):
        ev += i
print("total ev number: ",ev) 


######################################################  Password gen
small_let = []

for let in range(ord('a'), ord('z')+1):
    small_let.append(chr(let))
for cap in range(ord('A'), ord('Z')+1):
    small_let.append(chr(cap))

symb = ['!','@','$','%','&']

number =[]
for num in range(0,10):
    number.append(num)

pa = int(input("Enter the lenght of password: "))
n = int(input("Enthe the number of numbers: "))
s = int(input("Enthe the number of special char: "))

pa = pa-(n+s)

final_pass = []

while s>0:
    final_pass.append(random.choice(symb))
    s -= 1
while n>0:
    final_pass.append(random.choice(number))
    n -= 1
while pa>0:
    final_pass.append(random.choice(small_let))
    pa -= 1

random.shuffle(final_pass)

yes=""
for f in final_pass:
    yes +=str(f)

print(yes)







