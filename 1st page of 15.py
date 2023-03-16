#List Comprehension

#for loop version
'''result=[]
for i in range(11):
    result.append(i)
print(result)

#List Comprehension
print([i for i in range(11)])

#for loop version-->odd elements
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
print(result)
print([i for i in range(11)if i%2!=0])

result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
print([i if i%2!=0 else i**2 for i in range(11)])'''

#Practice1
'''mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#for loop --odd -->square it
#even -->cube it
result=[]
for row in mat:
    row_data=[]
    for ele in row:
        if ele%2!=0:
            row_data.append(ele**3)
        else:
            row_data.append(ele**2)
    result.append(row_data)
print(result)

#List Comprehension
print([ele**3 if ele%2!=0 else ele**2 for row in mat for ele in row])
print([[ele**2 if ele%2!=0 else ele**3 for ele in row] for row in mat])'''

#Practice2
'''mylist = [9, 3, 6, 1, 5, 8, 8, 2, 4, 7]
list_b = [6, 4, 6, 1, 2, 2]
result = []
for num in list_b:
    index = [i for i, x in enumerate(mylist) if x == num]
    for i in index:
        result.append((num, i))
print(result)'''

        #OR
'''mylist = [9, 3, 6, 1, 5, 8, 8, 2, 4, 7]
list_b = [6, 4, 6, 1, 2, 2]
result = []
for i in list_b:
    result.append((i,mylist.index(i)))
print(result)
#List comprehension
print([(i,mylist.index(i))for i in list_b])'''

            #OR
'''mylist = [9, 3, 6, 1, 5, 8, 8, 2, 4, 7]
list_b = [6, 4, 6, 1, 2, 2]
result = []

added_index=set()
for num in list_b:
    index=[i for i, x in enumerate(mylist)if x==num]
    for i in index:
        if i not in added_index:
            result.append((num,i))
            added_index.add(i)
print(result)'''

#Practice3
'''sentences=["a new world record was set","in the holy city of ayodhya","on the eve of diwali on tuesday","with over three lakh diya or earthen lamps","lits up simultaneously on the banks of the sarayu river"]
stopwords=['for','a','of','the','and','to','in','on','with','was']
def remove_stopwords(words):
    return [word for word in words if word not in stopwords]

def tokenize(sentence):
    words = sentence.lower().split()
    return remove_stopwords(words)

for sentence in sentences:
    words = tokenize(sentence)
    print(words)'''

                            #OR

'''sentences=["a new world record was set","in the holy city of ayodhya","on the eve of diwali on tuesday","with over three lakh diya or earthen lamps","lits up simultaneously on the banks of the sarayu river"]
stopwords=['for','a','of','the','and','to','in','on','with','was']
result=[]
for sentence in sentences:#"a new world was set"
    row_data=[]
    for word in sentence.split():
        if word not in stopwords:
            row_data.append(word)#new world record set
    result.append(row_data)
print(result)

print([[word for word in sentence.split()
        if word not in stopwords]for sentence in sentences])'''

#Practice4
#String of comma separated numbers.
'''inp = "3,2,6,5,1,4,8,9"
nums = inp.split(',')
num1=0
for i in nums:
	i = int(i)
	if i==5:
		break
	num1 += i
for j in nums[::-1]:
	j = int(j)
	if j==8:
		break
	num1 += j
num2=""
for k in range(inp.find('5'), inp.find('8')+1):
	if inp[k].isdigit():
		num2 += str(inp[k])
print(num1 + int(num2))'''

                        #OR
'''array=list(map(int,input().split(",")))
number1=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
number2=""
for i in l:
    number2+=str(i)
print(int(number2)+number1)'''

#Practice5
#String rotation
'''s=input().split(",")
stt=[]
num=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)#stt=[rhdt,ghftd]
    num.append(n)#numm=[246,1246]
def rotate (ss,n):#ss=rhdt,n=246
    n=str(n)
    s=0
    for i in n:#
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1] #rhdt t +rhd
    else:
        return ss[2:]+ss[:2] #ghftd ftdgh
for i in range(len(num)): #i=0
    print(rotate(stt[i],num[i]))'''

#Practice6
                            


