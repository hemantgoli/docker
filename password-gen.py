#!/bin/python

import random

len = int(input("Enter the lenght of password : "))

num = int(input("How many number you want in the password? : "))

spl = int(input("How many special characters you want? : "))

n = []
for i in range(0,10): n.append(i)

s = ["!","@","#","$","%","^","&","(",")"]

l =[]
for i in range(ord("a"),ord("z")+1): l.append(chr(i))
for i in range(ord("A"),ord("Z")+1): l.append(chr(i))

st=(len-(num+spl))

final = []

while st>0:
    final.append(random.choice(l))
    st-=1
while num>0:
    final.append(random.choice(s))
    num-=1
while spl>0:
    final.append(random.choice(n))
    spl-=1

random.shuffle(final)


for i in final: print(str(i))






