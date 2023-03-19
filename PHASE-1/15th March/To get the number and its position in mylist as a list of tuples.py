#Practice2(To get the number and its position in mylist as a list of tuples)
mylist = [9, 3, 6, 1, 5, 8, 8, 2, 4, 7]
list_b = [6, 4, 6, 1, 2, 2]
result = []

added_index=set()
for num in list_b:
    index=[i for i, x in enumerate(mylist)if x==num]
    for i in index:
        if i not in added_index:
            result.append((num,i))
            added_index.add(i)
print(result)

                                #OR
#for printing the repeated paired of postion and number
'''mylist = [9, 3, 6, 1, 5, 8, 8, 2, 4, 7]
list_b = [6, 4, 6, 1, 2, 2]
result = []
for i in list_b:
    result.append((i,mylist.index(i)))
print(result)
#List comprehension
print([(i,mylist.index(i))for i in list_b])'''
