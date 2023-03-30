'''
Given two list ,both having integer element ,write a python program using python lists to create and return a new list as per the rule given below:
if double of an element in list1 is present in list2,
then add it to the new list.
estimate time :20 minutes
sample input
list1-[11,8,23,7,25,15]
list2-[6,33,50,31,46,78,16,34]
expected output
new_list-[8,23,25]
'''
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
list3=[]
for i in list1:
    for j in list2:
        if i*2==j:
            list3.append(i)
print(list3)
