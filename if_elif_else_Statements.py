# if <condition>:
#     <operations>
# elif <condition>:
#     <operations>
# else:
#     <operations>

# < > == != <= >=
a = 10
b = 20
print(a<b)

##### * ##### * ##### * ##### * ##### *
print('#*#**#*#*#**#***#***#**#*#*#*#')
##### * ##### * ##### * ##### * ##### *

a = int(input("Enter a = "))
b = int(input("Enter b = "))
if a<b:
    print("b is greater")
elif b<a:
    print("a is greater")
else:
    print("both are equal")

##### * ##### * ##### * ##### * ##### *
print('#*#**#*#*#**#***#***#**#*#*#*#')
##### * ##### * ##### * ##### * ##### *

l = float(input("Enter l = "))
b = float(input("Enter b = "))

x = int(input("Enter 1 to calculate area 2 to calculate volume  "))
if x == 1:
    a = l*b
    print("The area is = ",a)
    
elif x == 2:
    h = float(input("Enter h = "))
    v = l*b*h
    print("The volume is = ",v)

else:
    print("Invalid input")

##### * ##### * ##### * ##### * ##### *
print('#*#**#*#*#**#***#***#**#*#*#*#')
##### * ##### * ##### * ##### * ##### *

a = float(input("Enter a = "))
b = float(input("Enter b = "))
o = input("Enter Operator + - * /  ")

if o == '+':
    print(a+b)
    
elif o == '-':
    print(a-b)
    
elif o == '*':
    print(a*b)
    
elif o == '/':
    print(a/b)

else:
    print("Invalid operator")


##### * ##### * ##### * ##### * ##### *
print('#*#**#*#*#**#***#***#**#*#*#*#')
##### * ##### * ##### * ##### * ##### *

physics = int(input("Enter physics marks = "))
chemistry = int(input("Enter chemistry marks = "))
math = int(input("Enter math marks = "))
english = int(input("Enter english marks = "))
nepali = int(input("Enter nepali marks = "))

total = physics+chemistry+math+english+nepali
per = total/5

if per >=80:
    print("The grade is = ",'A')

elif per >=60:
    print("The grade is = ",'B')
    
elif per >=50:
     print("The grade is = ",'C')
else:
    print("The grade is = ",'F')



# # Nested if
# if <condition>:
#     if <condition>:
#         <operations>



##### * ##### * ##### * ##### * ##### *
print('#*#**#*#*#**#***#***#**#*#*#*#')
##### * ##### * ##### * ##### * ##### *

a = float(input("Enter a = "))
b = float(input("Enter b = "))
o = input("Enter Operator + - * /  ")

if o == '+':
    print(a+b)
    
elif o == '-':
    print(a-b)
    
elif o == '*':
    print(a*b)
    
elif o == '/':
    if b == 0:
        print("The value of b can not be zero")
    else:
        print(a/b)

else:
    print("Invalid operator")


# and  &
# or   |
#True = 1
#False = 0

##### * ##### * ##### * ##### * ##### *
print('#*#**#*#*#**#***#***#**#*#*#*#')
##### * ##### * ##### * ##### * ##### *
a = True
b = False
print(a and b)

print('#*#**#*#*#**#***#***#**#*#*#*#')

a = True
b = False
print(a or b)


##### * ##### * ##### * ##### * ##### *
print('#*#**#*#*#**#***#***#**#*#*#*#')
##### * ##### * ##### * ##### * ##### *

a = float(input("Enter a = "))
b = float(input("Enter b = "))
o = input("Enter Operator + - * /  ")

if o == '+':
    print(a+b)
    
elif o == '-':
    print(a-b)
    
elif o == '*':
    print(a*b)
    
elif o == '/' and b != 0:
    print(a/b)
    
elif o == '/' and b == 0:
    print("Value of b can not be zero")
else:
    print("Invalid operator")


##### * ##### * ##### * ##### * ##### *
print('#*#**#*#*#**#***#***#**#*#*#*#')
##### * ##### * ##### * ##### * ##### *




##### * ##### * ##### * ##### * ##### *
print('#*#**#*#*#**#***#***#**#*#*#*#')
##### * ##### * ##### * ##### * ##### *





##### * ##### * ##### * ##### * ##### *
print('#*#**#*#*#**#***#***#**#*#*#*#')
##### * ##### * ##### * ##### * ##### *





##### * ##### * ##### * ##### * ##### *
print('#*#**#*#*#**#***#***#**#*#*#*#')
##### * ##### * ##### * ##### * ##### *






##### * ##### * ##### * ##### * ##### *
print('#*#**#*#*#**#***#***#**#*#*#*#')
##### * ##### * ##### * ##### * ##### *




##### * ##### * ##### * ##### * ##### *
print('#*#**#*#*#**#***#***#**#*#*#*#')
##### * ##### * ##### * ##### * ##### *




##### * ##### * ##### * ##### * ##### *
print('#*#**#*#*#**#***#***#**#*#*#*#')
##### * ##### * ##### * ##### * ##### *


##### * ##### * ##### * ##### * ##### *
print('#*#**#*#*#**#***#***#**#*#*#*#')
##### * ##### * ##### * ##### * ##### *