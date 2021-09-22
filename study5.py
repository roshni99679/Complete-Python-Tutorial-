#lamda filters and maps
#lamda is anonymous fn having 1 expression and multiple arguments

x= lambda a,b,c: a+b*c
print(x(10,2,4))
#use lambda fn inside a fn:
def fn(n):
    return lambda a:a*n
doubler=fn(2)
print(doubler(4))
tripler=fn(3)
print(tripler(4))

#filter--------------
def prime(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True
filtered=filter(prime,range(18))
print('prime numbers are',list(filtered))

#map fn---------------
def square(x):
    return x*x
w=square(4)
print(w)

def sq(y):
    return y*y
numbers=[1,2,3,4,5]
numsq=map(sq,numbers)
print(list(numsq))

#package camelcase- cmd: py -m pip install camelcase
#py -m pip list :to check list of packages we have in our system

import camelcase
x=camelcase.CamelCase()
a='hi this is a message to check first letter of each word is capitalized'
print(x.hump(a))