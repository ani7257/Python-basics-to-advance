#Problem1
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def merge_lists(l1,l2,n):
    if not l1:
        return l2
    if not l2:
        return l1

    current=l1
    count=1
    while current and count<n:
        current=current.next
        count+=1

    temp=current.next
    current.next=l2
    while l2.next:
        l2=l2.next
    l2.next=temp

    return l1

l1=Node(1)
l1.next=Node(2)
l1.next.next=Node(4)
l1.next.next.next=Node(3)
l1.next.next.next.next=Node(5)
l2=Node(9)
l2.next=Node(8)
l2.next.next=Node(11)

merged_list=merge_lists(l1,l2,2)

while merged_list:
    print(str(merged_list.data)+"->",end=" ")
    merged_list=merged_list.next

    
