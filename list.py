# # python collection
# list
# tuple
# set
# dict

# list
# -Contain Mupltiple data
# -Duplicate value
# -Indexing
# -Ordered
# -Mutable

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = [1,2,3,4,5,6,7,8,9]
b = ["Apple","Ball","Cat","Dog"]
print(type(a))
print(b)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

b = ["Apple","Ball","Cat","Dog","Apple"]
print(b)
print(b*2)

b = ["Apple","Ball","Cat","Dog","Apple"]
b[1]

b = ["Apple","Ball","Cat","Dog","Apple"]
b[0:30]

b = ["Apple","Ball","Cat","Dog","Apple"]
b[0:4:2]

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


a = ["Apple","Ball"]
b = ["Cat"]
print(b+a)

a = ["Apple","Ball"]
a[0] = "Ant"
print(a)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


a = "Hello World"
a = a.replace("Hello","hello")
print(a)

x = []
a = "Apple"
b = "Ball"
c = x+[a]
d = c+[b]
print(d)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = []
# a = list()
n = int(input("Enter n = "))
for i in range(n):
    x = input("Enter x = ")
    a = a+[x]
    
print(a)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = []
# a = list()
n = int(input("Enter n = "))
for i in range(n):
    x = int(input("Enter x = "))
    a = a+[x]

    
print(a)
print("Sum = ",sum(a))
print("Max = ",max(a))
print("Min = ",min(a))
print("Avg = ",sum(a)/n)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = [23432, 24242, 2423423, 224232, 23324]
a.sort()
print(a)

a = ["Ball","Apple","Zoo","Xray"]
a.sort()
print(a)


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = ['Apple', 'Ball', 'Xray', 'Zoo']
for i in a:
    print(i)


a = ['Apple', 'Ball', 'Xray', 'Zoo']
b == "Apple"
if b in a:
    print("Yes")

a = ['Apple', 'Ball', 'Xray', 'Zoo','apple']
b == "Apple"
if b in a:
    print("Yes")

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

c =0
a = ['Apple', 'Ball', 'Xray', 'Zoo','apple']
b == "Apple"
for i in a:
    if i ==b:
        c = c+1
        print("Yes")
print(c)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

c =0
a = ['Apple', 'Ball', 'Xray', 'apple','Zoo',]
b = input("Enter b = ")
for i in a:
    if i.lower() == b.lower():
        print(i)
        c = c+1
print(c)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# append()  insert()  extend()

a = []
b = "Ball"
a.append(b)
print(a)


a = []
a.append("Apple")
a.append("Ball")
a.append("cat")
print(a)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = []
# a = list()
n = int(input("Enter n = "))
for i in range(n):
    x = int(input("Enter x = "))
    a.append(x)
    
# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

print(a)
print("Sum = ",sum(a))
print("Max = ",max(a))
print("Min = ",min(a))
print("Avg = ",sum(a)/n)

a = ["Aplle","Ball","Cat"]
a.append("Dog")
print(a)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# insert()
a = ['Apple', 'Ball', 'Cat', 'Dog']
a.insert(1,'Fish')
print(a)


# extend()
a = [1,2,3,4]
b = [5,6,7,8,9]
a.extend(b)
print(a)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# del remove() pop()
a = ['Apple', 'Fish', 'Ball', 'Cat', 'Dog']
del a[0]
print(a)

a = ['Apple', 'Fish', 'Ball', 'Cat', 'Dog']
del a[0:3]
print(a)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# remove()
a = ['Apple', 'Fish', 'Ball', 'Cat', 'Dog']
a.remove('Apple')
print(a)

# remove()
a = ['Apple', 'Fish', 'Ball', 'Cat', 'Dog','Apple']
b = "Apple"
c = a.count(b)
for i in range(c):
    if b in a:
        a.remove(b)
    
    print(a)



# remove()
x = []
a = ['Apple', 'Fish', 'Ball', 'Cat', 'Dog','Apple']
b = "Apple"
l = len(a)
for i in range(l):
    if b != a[i]:
        x.append(a[i])
print(x)


# pop()
a = ['Apple', 'Fish', 'Ball', 'Cat', 'Dog','Apple']
b = a.pop(0)
print(a)

a = ['Apple', 'Fish', 'Ball', 'Cat', 'Dog','Apple']
a.index('Apple')


a = ['Apple', 'Fish', 'Ball', 'Cat', 'Dog','Apple']
for i in range(len(a)):
    if "Apple" == a[i]:
        print(i)


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

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



# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

info.split('\n')


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

info = 'Apple 200 4 800.Ball 4 200 800'
x = info.split('.')
print(x)
print(x[1])


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# list inside list
a = [[1,2,3,],[4,5,6],[7,8,9]]
print(a)

print(len(a))

a = [['Apple',200 ,4 ,800], ['Ball',4 ,200 ,800]]
a[1]

a = [['Apple',200 ,4 ,800], ['Ball',4 ,200 ,800]]
a[1]

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# list inside list
a = [[1,2,3,4],
     [4,5,6],
     [7,8,9]]
print(type(a))

a[0][0]


a = [['Apple',200 ,4 ,800], ['Ball',4 ,200 ,800]]
a[0] = ['Pineapple',100,2,200]
a


a = [['Apple',200 ,4 ,800], ['Ball',4 ,200 ,800]]
a[0][0] = "Pineapple"
a


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

print(info)
output = []
x = info.split('.')
print(x)

for i in x:
    y = i.split()
    output.append(y)
    
print(output)


a = 1
b = 2
c = 3
d = [a,b,c]
print(d)


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

info = []
add = 0
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter product name = ")
    price = int(input("Enter unit price = "))
    quantity = int(input("Enter quantity = "))
    total = price*quantity
    data = [name,price,quantity,total]
    info.append(data)
    add = add +total
    
print("The blling is = \n",info)
print("The total price is = ",add)


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another list example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #



