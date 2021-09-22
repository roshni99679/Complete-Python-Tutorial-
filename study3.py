list=['car','bus','bike','scooter']
def loop(x):
    print(x*4)
loop(list)

def map(crazy,list):
    for items in list:
        crazy(items)

map(loop,list) #functions as arguments

def my_fun(x):
    return 5*x
print(my_fun(3))
print(my_fun(4))
print(my_fun(5))

#lists tuples and dictionaries---------------

#lists are ordered ,changeable and allow dublicates
list=[1,'rosh',55.6,3j,True,1] #INT string float complex boolean
print(list)
print(len(list))
print(type(list))
print(list[0])
print(list[0:5]) #prints first to 4th elements
list[1]='roshni'
print(list)
list[0:3]=['rosh','khush','deep']
print(list)
list.insert(3,'geet') #inserts geet at 3rd index
print(list)
list.append('santosh')
print(list)
list.remove(3j)
print(list)

#tupples--------------
#tuples are ordered , unchangeable and allow duplicates
t=('apple','banana','mango',33,True)
print(type(t))
print(len(t))
print(t[0])
print(t[-1])  #last item of tupple(-1)
print(t[:])

#dictionary----------------------
#dic are unordered changeable and dont allow duplicates dic={'key':value}

dic={'rosh':20,'khush':True,'deep':'geet','fruits':['apple','mango']}
print(dic)
print(len(dic))
x=dic['khush']
print(x)
x=dic.get('khush')
print(x)
dic['khush']=19
print(dic)
dic.update({'deep':'santohs'})
print(dic)
dic['color']='black'
print(dic)
dic.pop('color')
print(dic)



