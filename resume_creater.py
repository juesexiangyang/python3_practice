#! /usr/bin/env python3.4
# -*- coding:UTF-8 -*-
from time import sleep
delay_time=3
name = str(input("please input your name: "))
age = str(input("ages: "))
school = str(input("school: "))
gratuated = str(input("gratuated in : "))
degree = str(input("degree: "))
major = str(input("major: "))
skills = str(input("skills: "))
print("OK,below is your resume,plz wait for 3 secs: \n\n")
sleep(delay_time)
print("          简历")
print("姓名:"+name)
print("年龄:"+age)
print("毕业院校:"+school)
print("哪年毕业:"+gratuated)
print("学位:"+degree)
print("专业:"+major)
print("掌握的技能:"+skills)

