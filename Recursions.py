#Convert function to recursive function
def sum(arg):
    result = 0
    for i in arg:
        result +=i
    return result

print(sum([1,2,3]))

print("\n***Converting to recursive function***")
#using test cases
def gSum(gArg):
    if len(gArg)==0:
        return 0
    else:
        return gArg[0] + gSum(gArg[1:])


print("TestCase 1: [1,2,3]",gSum([1,2,3]))
print("TestCase 2: [5,2,3]",gSum([5,2,3]))


#using integers from input
arg = input("\nEnter list separated by space: ")
arg = [int(f) for f in list(arg.split(' '))]

def gSum(arg):   
    if len(arg)==0:
        return 0
    else:
        return arg[0] + gSum(arg[1:])
print("Input Case List:",arg)
print(gSum(arg))



print("\nRecursive Function output")
#function outputs
def ise(n):
    if n==0:
        return True
    else:
        return iso(n-1)

def iso(n):
    if n==0:
        return False
    else:
        return ise(n-1)

print(iso(3))  #returns True
print(iso(2))  #returns False
print(ise(3))  #returns False
print(ise(2))  #returns True
