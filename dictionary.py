# dictionary
# -Contain Mupltiple data
# -Duplicate value
# -Indexing
# -Ordered
# -Mutable
# d = {<key>:<value>,<key>:<value>,<key>:<value>}

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

d = {'a':'apple',
     'b':'ball',
     'c':'cat'}
print(len(d))
print(type(d))


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

d = {'a':'apple',
     'b':'ball',
     'c':'cat',
    'A':'apple'}
print(d)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


d = {'a':'apple',
     'b':'ball',
     'c':'cat',
    'A':'apple'}
print(d['a'])
print(d['b'])



# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


d = dict()
d['a'] = 'Apple'
d['b'] = 'Ball'
print(d)



# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

z = {'a': 'Apple', 'b': 'Ball'}
z['a'] = 'apple'
print(z)


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


d = {}
d['Ram'] = 9856554543
d['Shyam'] = 9809778765
print(d)
print(d['Ram'])

d['Ram'] = 9878776765
print(d)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


info = dict()
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    phone = int(input("Enter phone = "))
    info[name] = phone
    
print(info)



# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


a = {'Ram': 9878776765, 'Shyam': 9809778765}
for i in a:
    print(i)

a = {'Ram': 9878776765, 'Shyam': 9809778765}
for i in a.values():
    print(i)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = {'Ram': 9878776765, 'Shyam': 9809778765}
for i in a.items():
    print(i)

l = [('Ram', 9878776765),('Shyam', 9809778765)]
print(dict(l))

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = {'Ram': 9878776765, 'Shyam': 9809778765}
n = int(input("Enter n = "))
for i in a.items():
   
    if n == i[1]:
        print(i[0])




# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


# del pop()
a = {'Ram': 9878776765, 'Shyam': 9809778765}
del a['Ram']
print(a)


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

#pop()
a = {'Ram': 9878776765, 'Shyam': 9809778765}
b = a.pop('Ram')
print(b)
print(a)

a = {('Ram','Hari'): 9878776765, 'Shyam': 9809778765}
print(a)

a[('Ram', 'Hari')]
print(a)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = {['Ram','Hari']: 9878776765, 'Shyam': 9809778765}
print(a)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# list inside dict
a = {'Ram': [9878776765,9808778765], 'Shyam': [9809778765,9089887865]}
a['Ram'][0]


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = {'Ram': [9878776765,9808778765], 'Shyam': [9809778765,9089887865]}
a['Hari'] = [9845778765,9808667654]
print(a)


a = {'Ram': [9878776765,9808778765], 'Shyam': [9809778765,9089887865]}
a['Ram'].append(9867665654)
print(a)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

d = {}
d['Ram'] = [9809778765, 9089887865]
d['Shyam'] = [9809778765,9089887865]
print(d)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

info = dict()
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    ntc_phone = int(input("Enter ntc phone = "))
    ncell_phone = int(input("Enter ncell phone = "))
    info[name] = [ntc_phone,ncell_phone]
    
print(info)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


a = {'Ram': ['Kathmandu', 'Dhading'], 
     'Shyam': ['Kathmandu', 'Nuwakot'],
    'Hari':['Jhapa','Bara']}
address = input("Enter address = ")
for i in a.items():
    if address.lower() == i[1][0].lower():
        print(i)


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = {'Ram': ['Kathmandu', 'Dhading'], 
     'Shyam': ['Kathmandu', 'Nuwakot'],
    'Hari':['Jhapa','Bara']}
a.items()

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# tuple inside list
a = {'Ram': ('Kathmandu', 'Dhading'), 
     'Shyam': ('Kathmandu', 'Nuwakot'),
    'Hari': ('Jhapa','Bara')}

for i in a.items():
    print(i)

a['Ram'] =('Kathmandu', 'Dang')
print(a)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

# dict inside list
a = [{'Name':'Ram','Address':'Kathmandu'},
   {'Name':'Shyam','Address':'Bara'},
    {'Name':'Nabin','Address':'Bhaktapur'}]
print(a)
print(a[0])

for i in a:
    print(i)

for i in a:
    for j in i.items():
        print(j)


for i in a:
    print(i['Name'])

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


a = [{'Name': 'Ram', 'Address': ['Kathmandu','Patan']}, 
     {'Name': 'Shyam', 'Address': ['Bara','Saptari']}, 
     {'Name': 'Nabin', 'Address': ['Bhaktapur','Nuwakot']}]
b = {'Name': 'Ram', 'Address': ['Kathmandu','Patan']}
a.append(b)
print(a)

print(a[0]['Address'][0])


# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = [{'Name': 'Ram', 'Address': {'Per':'Kathmandu','Tem':'Patan'}}, 
     {'Name': 'Shyam', 'Address': {'Per':'Bara','Tem':'Saptari'}}, 
     {'Name': 'Nabin', 'Address':{'Per':'Saptari','Tem':'Kathmandu'}}]
print(a)

print(a[0]['Address']['Per'])
# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #

a = {1:{'Name': 'Ram', 'Address': {'Per':'Kathmandu','Tem':'Patan'}}, 
     2:{'Name': 'Shyam', 'Address': {'Per':'Bara','Tem':'Saptari'}}, 
     3:{'Name': 'Nabin', 'Address':{'Per':'Saptari','Tem':'Kathmandu'}}}
print(a)

a[4] ={'Name': 'Nabin', 'Address':{'Per':'Saptari','Tem':'Kathmandu'}}
print(a)


a[4]['Address']['Per'] = 'Patan'
print(a)

# * # * # * # * # * # * # * # * # * # * # * # * # * #
print("!!! --- This is another dictionary example --- !!!")
# * # * # * # * # * # * # * # * # * # * # * # * # * #


# WAP to make dict inside dict
# WAP to make list inside dict
# WAP to make dict inside list
