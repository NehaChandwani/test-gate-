'''Create a function that accepts 3 parameters and checks for equality between any two of them.

Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal 
to any of the others.
Modify your function so that strings can be compared to integers if they are equivalent. For example, 
if the following values are passed to your function:'''
def equality(Var1,Var2,Var3):
    Var1=input("Enter first number")
    Var1=int(Var1)
    Var2=input("Enter second number")
    Var2=int(Var2)
    Var3=input("Enter third number")
    Var3=int(Var3)
    if(Var1==Var2==Var3):
        return True
    else:
        return False
a=0
b=0
c=0
output1=equality(a,b,c)
print(output1)

