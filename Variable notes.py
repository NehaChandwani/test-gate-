#string="Hello"+ 1(Will give error )
PI=3.14#Constant declared in begining to be used throughout the program. 
string="Hello"+"1"
string="Hello+1"
print(string)
#All the variables which are not included in a function they are called as global can acces them from anywhere  .
#I can declare constant if I want to use anywhere in a program 
r=int(input("Enter r"))
area=PI*r*r
print(area)
#Example of local variable 
def area()
    global r 
    print(r)
    newvar="World"
    print(newvar)
    return
area()
#We can also declare variable as 
one,two,three=1,2,3
print(one)
print(two)
print(three)
five=5
#Everything to left is what you are giving value to 
#right= What the value is 
print(five)
#Counting variables 
count=0 
print(count)
count=count+1
count+=1 # this is same as count+1
print(count)
count=count*3 # this is same as  count*=3
print(count)
