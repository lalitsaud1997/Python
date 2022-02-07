# Loop
# -For
# -While 

# for loop
# range()
for i in range(5):            #for (i =0;i<5;i++)
    print(i,"Hello World")


 # for loop
# range()
for i in range(1,5):            #for (i =1;i<5;i++)
    print(i,"Hello World")

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #
    # for loop
# range()
for i in range(1,5,2):            #for (i =1;i<5;i=i+2)
    print(i,"Hello World")

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

n = int(input("Enter n = "))
for i in range(1,11):
    print(i*n)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

n = int(input("Enter n = "))
for i in range(1,11):
    print(n,"*",i,"=",i*n)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

s = 0
n = int(input("Enter n = "))
for i in range(n):
    x = int(input("Enter x = "))
    s = s+x
print(s)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# 4! = 1*2*3*4
fac = 1
n = int(input("Enter n = "))
for i in range(1,n+1):
    fac = fac*i
print(fac)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = "Python"
for i in a:
    print(a)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = "Python"
for i in a:
    print("Hello World")

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = "Python"
l = len(a)
for i in range(l):
    print(a[i])

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

s = ""
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    phone = input("Enter phone = ")
    info = name+" "+phone 
    s = s + info +"\n"
print(s)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

n = int(input("Enter n = "))
result = ""
for i in range(n):
    name = input("Enter name = ")
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
#     info = name + " " + str(physics) 


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


for i in range(1,21):
    if i%2 != 0:
        print(i)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

for i in range(1,51):
    if i%5 == 0:
        print(i)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# control statement
# break
# continue
# pass

for i in range(10):
    if i == 5:
        break
    else:
        print(i)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = "Hello World"
for i in a:
    if i == ' ':
        break
    print(i)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

for i in range(10):
    if i == 5:
        continue
    else:
        print(i)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = "Hello World I am Python"
for i in a:
    if i == ' ':
        continue
    print(i,end= "")       

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

for i in range(1,51):
    if i % 5 !=0:
        continue
    else:
        print(i)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

n = int(input("Enter n = "))
if n>2:
    for i in range(2,n//2):
        if n%i ==0:
            print("This is composite no")
            break
    else:
        print("This is prime no")
else:
    print("The no should be greater than 2")


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# 0 1 1 2 3 5 8 13     

for i in range(5,-1,-1):
    print(i)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = "Python"
l = len(a)
print(l)
for i in range(l-1,-1,-1):
    print(a[i],end = "")

# Nested for
# for <>:
#     for <>:

for i in range(3):
    for j in range(3):
        print(i,j)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

for i in range(3):
    for j in range(3):
        for k in range(3):
            print(i,j,k)

# # while loop
# while <condition>:
#     <operations>     
#infiniti loop
# while True:
#     print("Hello World")

a = 10
b = 2
x = a>b
print(x)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

n = 0
while n<5:
    print(n)
    n = n+1

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

n = 0
while n<5:
    print("Hello World")
    n = n+1

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

n = 1
while n<5:
    print(n,"Hello World")
    n = n+1

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

n = 1
while n<5:
    print(n,"Hello World")
    n +=2

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

i = 1
n = int(input("Enter n = "))
while i<=10:
    print(n,"*",i,"=",i*n)
    i = i+1

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

s = 0
i = 0
n = int(input("Enter n = "))
while i<n:
    x = int(input("Enter x = "))
    s = s+x
    i = i+1
print(s)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = "Python"
l = len(a)
i = 0
while i<l:
    print(a[i])
    i = i+1

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = "Python"
l = len(a)-1
i = 0
while l>=i:
    print(a[l],end = "")
    l = l-1

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


n = int(input("Enter n = "))
m = 2
if n>m:
    while m<n:
        if n%m ==0:
            print("This is composite no")
            break
        m = m +1
    else:
        print("This is prime no")
else:
    print("The no should be greater than 2")


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


# Control statements in while loop
# break

while True:
    print("Hello World")
    break
    
while 10<20:
    print("10 is greater than 20")
    break

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


a = "Hello World"
l = len(a) -1
k = 0
while k<l:
    if a[k] == " ":
        break
    print(a[k])
    k = k+1

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


a = "Hello World"
l = len(a) -1
k = 0
while k<=l:
    if a[k] == " ":
        k = k+1        
        continue
    print(a[k],end = "")
    k = k+1

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another loop example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

    # pass