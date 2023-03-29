#Practice2
list1 = ['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
list2 = ['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']

new_list = []
for i in range(len(list1)):
    if list1[i] is None:
        new_list.append(list2[-(i+1)])
    else:
        new_list.append(list1[i])

new_str = ' '.join([word for word in reversed(new_list)])
print(new_str)


