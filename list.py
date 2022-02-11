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



a = ['Apple', 'Ball', 'Xray', 'Zoo']
for i in a:
    print(i)