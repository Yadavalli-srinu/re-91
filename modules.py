#match
import re
n = input("Enter password:")
res=re.match("srinu123",n)
if res:
    print("Enter pasword===")
    n1=input("Enter password:")
    res1=re.match("srinu1234",n1)
    if res1:
        print("Login Sucessfully")
    else:
        print("Wrong Password")
else:
    print("Wrong Paaword")
#output
# Enter password:srinu1234
# Enter pasword===
# Enter password:srinu123456
# Login Sucessfully

#fullmatch
import re
n = input("Enter password:")
res=re.match("srinu123",n)
if res:
    print("Enter pasword===")
    n1=input("Enter password:")
    res1=re.fullmatch("srinu1234",n1)
    if res1:
        print("Login Sucessfully")
    else:
        print("Wrong Password")
else:
    print("Wrong Paaword")

#output
# Enter password:srinu123
# Enter pasword===
# Enter password:srinu1234
# Login Sucessfully

import re
data="yadavalis9@gmail.com"
result=re.findall(r"\d",data)
print(result)
#output
#['9']

import re
data="yadavalis9@gmail.com"
result=re.findall(r"\d",data)
for i in result:
    print(i)
#output
#9

import re
data="yadavalis9@gmail.com"
result=re.findall(r"\D",data)
for i in result:
    print(i)
#output
# y
# a
# d
# a
# v
# a
# l
# i
# s
# @
# g
# m
# a
# i
# l
# .
# c
# o
# m
import re
data="yadavalis9@gmail.com"
result=re.findall(r"\W",data)
for i in result:
    print(i)
#output
# @
# .

import re
data="yadavalis9@gmail.com"
result=re.findall(r"\S",data)
for i in result:
    print(i)
#output
# y
# a
# d
# a
# v
# a
# l
# i
# s
# 9
# @
# g
# m
# a
# i
# l
# .
# c
# o
# m



import re
a = "python"
res=re.findall(r"[aeiouAEIOU]",a)
print(res)
#output
#['o']
import re
a = "python mobile number 1234567890"
res=re.findall(r"\d",a)
print(res)
#output
#['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
import re
a = "python mobile number 1234567890"
res=re.sub(r"\d","#",a)
print(res)
#output
#python mobile number ##########
import re
a = "python mobile number 1234567890"
res=re.sub("python","java",a)
print(res)
#output
#njava mobile number 1234567890
import re
a = "python mobile number 1234567890"
res=re.findall(r"\D*",a)
print(res)
#output
#['python mobile number ', '', '', '', '', '', '', '', '', '', '', '']
import re
a = "python mobile number 1234567890"
res=re.findall(r"\D+",a)
print(res)
#output
#['python mobile number ']
import re
a = "python mobile number 1234567890"
res=re.findall(r"\D?",a)
print(res)
#output
#['p', 'y', 't', 'h', 'o', 'n', ' ', 'm', 'o', 'b', 'i', 'l', 'e', ' ', 'n', 'u', 'm', 'b', 'e', 'r', ' ', '', '', '', '', '', '', '', '', '', '', '']
import re
n = input("Entrer mobile number:")
res=re.fullmatch(r"[6-9][0-9]{9}",n)
if res:
    print("Valid mobile number")
else:
    print("Invalid  mobile number")

#output
# Entrer mobile number:1234567890
# Invalid  mobile number
# Entrer mobile number:6301942115
# Valid mobile number
