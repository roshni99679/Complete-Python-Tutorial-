#list comprehension---------------
fruits=['apple','mango','banana','cherry']
newfruit=[]
for f in fruits:
    if 'a'in f:
        newfruit.append(f)
print(newfruit)

newfruit=[f for f in fruits if 'a'in f]   #alternative
print(newfruit)

newfruit=[f for f in fruits if f!='mango']   #alternative
print(newfruit)
newfruit=[f for f in range(10)]
print(newfruit)
newfruit=[f.upper() for f in fruits]
print(newfruit)
newfruit=[f if f!='cherry' else 'oranges' for f in fruits]
print(newfruit)
n=[x for x in range(10)if x<5]
print(n)




