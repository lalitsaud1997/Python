# def <function_name>():
#     <operation>
    
# <function_name>()
# print()
# int()
# str()
# float()
# type()

# user defined
def hello():
    print("Hello World")
    
hello()
hello()

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another function example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

def cal():
    l = int(input("Enter l = "))    #local variable
    b = int(input("Enter b = "))
    h = int(input("Enter h = "))
    v = l*b*h
    print(v)

cal()

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another function example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

l = int(input("Enter l = "))    #global variable
b = int(input("Enter b = "))
h = int(input("Enter h = "))
def cal():
    v = l*b*h
    print(v)

cal()

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another function example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

def cal():
    global l
    l = int(input("Enter l = "))    #local variable
    b = int(input("Enter b = "))
    h = int(input("Enter h = "))
    v = l*b*h
    print(v)

cal()
print(l)


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another function example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

x = int(input("Enter 1 for area 2 for volume = "))
if x ==1:
    l = int(input("Enter l = "))    #local variable
    b = int(input("Enter b = "))
    a = l*b
    print("The area is = ",a)
elif x == 2:
    l = int(input("Enter l = "))    #local variable
    b = int(input("Enter b = "))
    h = int(input("Enter h = "))
    v = l*b*h
    print(v)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another function example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

def area():
    l = int(input("Enter l = "))    #local variable
    b = int(input("Enter b = "))
    a = l*b
    print("The area is = ",a)
def volume():
    l = int(input("Enter l = "))    #local variable
    b = int(input("Enter b = "))
    h = int(input("Enter h = "))
    v = l*b*h
    
    
x = int(input("Enter 1 for area 2 for volume = "))
if x ==1:
    area()
elif x == 2:
    volume()
    
else:
    print("Invalid number")

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another function example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

def area():
    a = l*b
    print("The area is = ",a)
    
def volume():
    h = int(input("Enter h = "))
    v = l*b*h
    
    
x = int(input("Enter 1 for area 2 for volume = "))
l = int(input("Enter l = "))    #global variable
b = int(input("Enter b = "))

if x ==1:
    area()
elif x == 2:
    volume()
    
else:
    print("Invalid number")


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another function example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# function with no argument and no return type
# function with argument and no return type
# function with no argument and return type
# function with argument and return type

# function with argument and no return type

def hello(a):        #parameter
    print(a)
    
hello("Hello World")  #Argument


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another function example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# function with argument and no return type

def area(l,b):   #parameter
    a = l*b
    print(a)

area(10,5)    #Argument

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another function example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# function with argument and no return type
def cal(x,y,z):
    v = x*y*z
    print(v)


l = int(input("Enter l = "))    #local variable
b = int(input("Enter b = "))
h = int(input("Enter h = "))

cal(l,b,h)


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another function example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def cal():
    a = float(input("Enter a = "))
    b = float(input("Enter b = "))
    o = input("Enter Operator + - * /  ")
    if o == '+':
        add(a,b)
    elif o == '-':
        sub(a,b)
    elif o == '*':
        mul(a,b)
    elif o == '/' and b != 0:
        div(a,b)
    elif o == '/' and b == 0:
        print("Value of b can not be zero")
    else:
        print("Invalid operator")
cal()

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another function example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# Return Type function

def Cal():
    l = int(input("Enter l = "))
    b =  int(input("Enter b = "))
    h =  int(input("Enter h = "))
    v = l*b*h
    return v

print(Cal())

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another function example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

l = int(input("Enter l = "))
b =  int(input("Enter b = "))
def volume():
    h =  int(input("Enter h = "))
    v = l*b*h
    return v

def area():
    a = l*b
    return a
volume = volume()
area = area()
print(area,volume)

