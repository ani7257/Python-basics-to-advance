#list--ordered--default index
'''list1=[]
print(list1,type(list1))
list2=[10,20,30.40]
print(list2,type(list2))
list3=[10,20.2,30+3j,True,"python"]
print(list3,type(list3))
list4=list([100,200,300,400])
print(list4,type(list4))
list5=[101,201,301,401]
print(list5,type(list5))
list5.append(501)
print(list5,type(list5))
list5.extend([601,701,801])
print(list5,type(list5))
list5.insert(0,51)
print(list5,type(list5))
list5.insert(4,350)
print(list5,type(list5))
list5.remove(801)
print(list5,type(list5))
list5.pop()
print(list5,type(list5))
list5.pop(0)
print(list5,type(list5))
del list5[1]
print(list5,type(list5))'''

#Practice1
'''def function(str1):
    l_count = 0
    d_count = 0
    for i in str1:
        if i.isalpha():
            l_count=l_count+1
        elif i.isdigit():
            d_count=d_count+1
        else:
            continue
    return[l_count,d_count]
#s=input()
#print(function(s))
print(function("Infosys 123"))
print(function("ABCEFG"))'''

#Practice2
'''def find_pairs_of_numbers(list, n):
    pairs_count = 0
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] + list[j] == n:
                pairs_count=pairs_count+1
    if pairs_count == 0:
        return 0
    else:
        return pairs_count

result= find_pairs_of_numbers([1,2,7,4,5,6,0,3],6)
print(result)'''

                    #OR
'''def find_pairs_of_numbers(num_list, n):
    count = 0
    for x in num_list:
        index=num_list.index(x)+1 #index=1
        for y in range(index,len(num_list)):
            if x+num_list[y]==n:
                count+=1
    return count
num_list=[1,2,7,4,5,6,0,3]
n=6
print(find_pairs_of_numbers(num_list,n))'''

#Practise3
'''def function1(str1):
    length=len(str1)
    if length<2:
        return (-1)
    elif length==2:
        return (str1*2)
    else:
        return(str1[0:2]+str1[-2:])
str1=input()
print(function1(str1))'''

#Practice4
'''def add_ing(word):
    if len(word)<3:
        return word
    elif word[-3:]=='ing':
        return word+'ly'
    else:
        return word+'ing'

word1='sleep'
print(add_ing('sleep'))
word1='amazing'
print(add_ing('amazing'))
word1='is'
print(add_ing('is'))'''

#Practise5
'''def check_double(number):
    str_num=str(number)
    str_double=str(number*2)
    if len(str_num)!=len(str_double):
        return False
    for digit in str_num:
        if digit not in str_double:
            return False
        else:
            str_double=str_double.replace(digit,'',1)
    return True
n=input()
print(check_double(n))'''

                    #OR
'''def check_double (number):
    num1=str(number*2)
    number=str(number)
    count=0
    for x in number:
        if x in num1:
            count+=1
        else:
            return False
    if count==len(number):
        return True
print(check_double (245))
print(check_double (125874))'''

#Practice6
'''list_of_marks=[12,18,25,24,2,5,18,20,20,21]
def find_more_than_average():
    global list_of_marks
    marks=0
    count=0
    for x in list_of_marks:
        marks+=x
    average=marks/len(list_of_marks)
    for x in list_of_marks:
        if x>average:
            count+=1
    percentage=(count*100)/len(list_of_marks)
    return percentage
def generate_frequency():
    freq=[]
    global list_of_marks
    for x in range(26):
        count=0
        for y in list_of_marks:
            if x == y:
                count+=1
        freq.append(count)
    return  freq
def sort_marks():
    global list_of_marks
    list_of_marks=sorted(list_of_marks)
    return list_of_marks
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())'''

#Practise7
'''def translate(dict1,list1):
    list2=[]
    for i in list1:
        list2.append(dict1[i])
    return list2
dict1={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
list1=["merry","christmas","and","happy","new","year"]
print(translate(dict1,list1))'''

#Practise8
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



