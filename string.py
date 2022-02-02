 ##### * ##### * ##### * ##### * ##### *
a = "Hello World"
print(a)
print(type(a))

#output:
# Hello World
# <class 'str'>

 ##### * ##### * ##### * ##### * ##### *

a = "Hello World"
print(a[-1])
print(a[0:5])
print(a[0:5:2])

#output:
# d
# Hello
# Hlo

##### * ##### * ##### * ##### * ##### *
a = "Hello World"
b = a[0:5]
c = a[5:]
print(b)
print(c)

#output:
# Hello
#  World

##### * ##### * ##### * ##### * ##### *

# string formatting
a = "Ram"
b = 10
c = "Hello I am "+a+" I am "+str(b)
print(c)

#output:
# Hello I am Ram I am 10


##### * ##### * ##### * ##### * ##### *

# string formatting
a = "Ram"
b = 10
c = f"Hello I am {a} I am {b}."
print(c)

#output:
# Hello I am Ram I am 10.

##### * ##### * ##### * ##### * ##### *

info = ""
add = 0
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter product name = ")
    price = int(input("Enter unit price = "))
    quantity = int(input("Enter quantity = "))
    total = price*quantity
    s = f"{name} {price} {quantity} {total}\n"
    info = info+s
    add = add+total
    
print("The blling is = \n",info)
print("The total price is = ",add)

#output:
# Enter n = 2
# Enter product name = apple
# Enter unit price = 30
# Enter quantity = 2
# Enter product name = banana
# Enter unit price = 24
# Enter quantity = 2
# The blling is = 
#  apple 30 2 60
# banana 24 2 48

# The total price is =  108

##### * ##### * ##### * ##### * ##### *

a = "Python"
print(len(a))
print(a[5::-1])
print(a.upper())
print(a.lower())

#output:
# 6
# nohtyP
# PYTHON
# python

##### * ##### * ##### * ##### * ##### *

a = "Hello World I am Python"
if "Hello" in a:
    print("Yes")
else:
    print("No")

#output:
# yes

##### * ##### * ##### * ##### * ##### *

a = "Hello World I am Python".lower()
if "HEllo".lower() in a:
    print("Yes")
else:
    print("No")

#output:
# yes

##### * ##### * ##### * ##### * ##### *
a = "Hello World I am Python".lower()
print(a)

#output:
# hello world i am python
##### * ##### * ##### * ##### * ##### *

b = "HEllo".lower()
print(b)

#output:
# hello

##### * ##### * ##### * ##### * ##### *

a = "Hello World I am Python"
x = a.lower()
b = input("Enter value for search = ")
y = b.lower()

if y in x:
    print("Yes")
    print(x.count(y))
else:
    print("No")

#output:
#Enter value for search = am
#Yes
#1

##### * ##### * ##### * ##### * ##### *

# replace()
a = "Python Hello World I am Python"
b = a.replace("Python ","PYTHON ")
print(b)

#output:
#PYTHON Hello World I am Python

##### * ##### * ##### * ##### * ##### *

# replace()
a = "Hello World I am Python"
b = a.replace("Python","")
print(b)

#output:
#Hello World I am
##### * ##### * ##### * ##### * ##### *

a = "Hello World I am Python"
x = a.lower()
b = input("Enter value for search = ")
y = b.lower()

if y in x:
    print("Yes")
    print(x.count(y))
#     replace()
else:
    print("No")

#output:
#Enter value for search = i
#Yes
#1

##### * ##### * ##### * ##### * ##### *
##### * ##### * ##### * ##### * ##### *
##### * ##### * ##### * ##### * ##### *
               