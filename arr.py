#to create an array always import array module
#3 ways: import array, import array as arr(most common), from array import *

#import array
import array
#array-1 is name of module array 2 is type of constructor "b" is a typecode which specifies type of elements data will hold
r=array.array('b', [19,29,39,49,59,69])

print(r)

import array as arr
#arr is alias name
a=arr.array("q", [14, 24, 34, 44, 54, 64])
print(a)

from array import *
s=array("q", [1, 2, 3, 4, 5, 6])
#constractor name only is used
print(s)


#accessing array elements **use index
print(s[4])
print(r[0])
print(a[-1])


'''arrays operations'''
#arrays are mutable i.e they are changeable

#(1)finding the length of an array;len functions
x=arr.array('q', [1, 11, 8, 5,7,145])
print(len(x))

#adding elements in an array:add elements using append(), insert() or extend([])
r.append(123)
s.extend([4,8,9,223])
x.insert(3,3)

print(r)
print(s)
print(x)
#removing elements in an array:pop(),remove()
a.pop()
s.pop(4)
x.remove(5)

print(a)
print(s)
print(x)

#array concatenation: use (+) symbol also the typecodes of the arrays should be the same
y=arr.array('q',)

y= a+s

print(y)

#array slicing
print(y[5:])
print(s[0:3])
print(s[:-4])
print(s[::-1])
#looping through an array

'''for z in x[0:4]:
    print(z)'''


m=0
while m<len(a):
    print(a[m])
    m=m+1