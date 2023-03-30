#Linear Search in Python
def LinearSearch(array, n, x):
    #Going through array sequentially
    for i in range(0,n): #0 to 4
        if (array[i]==x):
            return i
    return -1
array=[2,4,0,1,9]
x=10#key
n=len(array)
result=LinearSearch(array,n,x)
if(result==-1):
    print("Element not found")
else:
    print("Element found at index: ", result)
