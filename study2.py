if 5>3:
    print("yes")

#variables and names
x=5
y="roshni"
print(x,y)
x=3
x="john"
print(x)
#casting the datatype
p=str(4)
q=int(4)
r=float(4)
print(p,q,r)
print(type(p) ,type(q), type(r))
#variables must start with underscore or letter and not a number
#variable can contain letters numbers and underscore
#variables are case sensitive
_car="honda"
cup="jesf"
print(_car,cup)
#assigning multiple values to a variable
x,y,z="apple","mango",33
print(x,y,z)
print(x)
#assigning same values to varios variables
rosh=khush=deep=33
print(deep)

#strings
x='''oranges 
are 
orange in
color'''
print(x)
print(x[5])
print(len(x))
print('are'in x)
print('ythr'in x)
#slice a str
x="i am roshni @rosh053    "
y='hello'
print(x[2:3])
print(x[:3])
print(x[0:])
print(x[:])
print(x[-8:-3])
print(x.upper())
print(x.lower())
print(x.strip())
print(x)
print(x.replace('r','k'))
print(x+' '+y)
print(x.strip() +' '+y)

#conditional operators
a=11
b=44
c=23
if(a>b):
    print("a is greater")
else:
    print ('b is greater')
#both conds should satisfy
if a>b and c>a:
    print(b)
else:
    print(b)
#if any one of the condns is satisfied it goes to if wala print
if a>b or c>a:
    print(a)
else:
    print(b)

#functions in python--------------------------------------

def trialfunction(x,y): #defining a fn by passing a parameter
    print(x+' '+y)
trialfunction('ROSHNI','pretty')  #calling a fn by passing argument

#for loop and while loop--------------------------------------

num=[1,2,3,4,5,622,100] #list
for x in num:
    if x==5:
        continue
    print(x)
    if x==622:
        break
for l in range(1,5):
    print(l)
for w in range(6):
    print(w)




x='banana'
for p in x:
    print(p)
#while loop-----------------------
i=1
while(i<6):
    print(i)
    if i==4:
        break
    i+=1

i=0
while(i<6):
    i += 1

    if i==4:
        continue
    print(i)


