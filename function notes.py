#functions 
''' Syntax:- 
def Functionname(Input):
     Action 
     return output 
     More code # This is a part of function as it is indented 
More code # This is not a part of function as it is not indented'''
def addOne(Number):
    Number+=1
    return Number

Var=0
print(Var) # output is 0 
Var2 = addOne(Var)
print(Var2) #output is 1 
Var3 = addOne(Var2)
print(Var3) 
Var4 = addOne(2)
print(Var4)
Var5=addOne(2+3)
print(Var5)

def addOneAddTwo(Number1,Number2):
   output=Number1+Number2
   return output
a=10
b=20
c=addOneAddTwo(a,b)
print(c)
    