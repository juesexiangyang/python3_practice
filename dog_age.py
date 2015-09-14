#! /usr/bin/env python3.4
age = int(input("Age of the dog: "))
print()
if age < 0:
    print("You must bu kidding me~")
elif age == 1:
    print("About 14 human years")
elif age == 2:
    print("About 22 human years")
else:
    age=22+(age-2)*5
    print("About "+str(age)+" human years")

input('press Return>')
