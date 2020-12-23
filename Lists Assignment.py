myUniquelist=[]
myLeftovers=[]
def addlist(newthing):
    if newthing in myUniquelist:
        myLeftovers.append(newthing)
        return False
    else:
        myUniquelist.append(newthing)
        return True
print(myUniquelist)
addlist("dog")
addlist("cat")
addlist("lion")
addlist("dog")
addlist("giraffe")
addlist("snake")
addlist("giraffe")
addlist("snake")   
print(myUniquelist)
print(myLeftovers)

