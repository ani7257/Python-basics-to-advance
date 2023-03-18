#Practise8(To find the number of distinct subarrays in an array of position integers such that the sum of the subarray is an odd integer)
n1=int(input("Enter a value for n1"))
n2=int(input("Enter a value for n2"))
array=[i for i in range(n1,n2+1)]
print(array)
l1=[array[i:j+1] for i in range(len(array)) for j in range(i,len(array))]
print(l1)
c=0
for i in l1:
    if sum(i)%2!=0:
        c+=1
print(c)
result=[]
for i in range(n1,n2+1):
    result.append(i)
print(result)
result=[i for i in range(n1,n2+1)]
print(result)

array=[i for i in range(n1,n2+1)]
result=[]
for i in range(len(array)):
    for j in range(i,len(array)):
        result.append(array[i:j+1])
print(result)
result=[array[i:j+1] for i in range(len(array))
        for j in range(i,len(array))]
print(result)
