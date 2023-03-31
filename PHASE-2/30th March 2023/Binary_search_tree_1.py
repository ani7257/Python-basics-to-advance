#Binary Search Tree operations in Python
class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key)+"->",end=' ')
        inorder(root.right)
def insert(node,key):#node=1000,key=6
    if node is None:
        return Node(key)#3000
    if key<node.key:#1<3
        node.left=insert(node.left,key)#None,1
    else:
        node.right=insert(node.right,key)
    return node
def minValueNode(node):#6000
    current=node#6000
    #Find the leftmost leaf
    while(current.left is not None):
        current=current.left#current=4000
    return current
def deleteNode(root,key):#4000 4
    if root is None:
        return root
    if key<root.key:#7<7
        root.left=deleteNode(root.left,key)
    elif(key>root.key):#6>6
        root.right=deleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.right#temo=None
            root=None
            return temp#
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minValueNode(root.right)
        root.key=temp.key#6000.key=7
        root.right=deleteNode(root.right,temp.key)
    return root
root=None
root=insert(root,8)
root=insert(root,3)
root=insert(root,1)
root=insert(root,6)
root=insert(root,7)
root=insert(root,10)
root=insert(root,14)
root=insert(root,4)
print("Inorder traversal: ", end=' ')
inorder(root)
print("\n Delete 10")
root=deleteNode(root,10)
#print("Inorder Traversal:",end=' ')
inorder(root)
