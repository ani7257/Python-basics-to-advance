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
def deleteNode(root,key):
    if root is None:
        return root
    if key<root.key:
        root.left=deleteNode(root.left,key)
    elif(key>root.key):
        root.right=deleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
root=None
root=insert(root,8)#1000
root=insert(root,3)#1000,3
root=insert(root,1)#1000,1
root=insert(root,6)#1000 6
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
