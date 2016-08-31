#!/usr/bin/env python3
# Created by Omri Gabay, 8/31/2016
# Simple program to switch the first letter of the first and last name, a la Runny Babbit

print("Enter your name here: ")
name = input()

s = list(name)
print(s)
ind = name.rfind(" ")
print(ind)
ind = ind + 1
temp = s[ind]
s[ind] = s[0]
s[0] = temp

print("And here is your name with the first letters switched: ")
print("".join(s))
