#Basic
for i in range(151):
    print(i)

#Multiples of Five
for i in range(5,1005,5):
    print(i)

#Counting, the dojo way
for i in range(1,105):
    if i % 5 == 0:
        print(i, "Coding")
    elif i % 10 ==0:
        print(i, "Coding")

#Whoa, that sucker's huge
for i in range(0, 500):
    if i % 2 !=0:
        print(i)

#Coundown by fours
for i in range(2018,0,-4):
    print(i)

#Flexible Counts
lownum = 2
highnum = 9
mult = 3
for i in range(lownum,highnum +1):
    if i % mult == 0:
        print(i)