#Practice4(String of comma separated numbers)
array=list(map(int,input().split(",")))
number1=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
number2=""
for i in l:
    number2+=str(i)
print(int(number2)+number1)

                            #OR
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
