class BSTtreeNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def inoderTraversal(root):
    if root:
        inoderTraversal(root.left)
        print(str(root.data)+" ",end=' ')
        inoderTraversal(root.right)
def insertBST(node,new_data):
    if node is None:
        return BSTtreeNode(new_data)
    if new_data>node.data:
        node.right=insertBST(node.right,new_data)
    else:
        node.left=insertBST(node.left,new_data)
    return node
def MinimumValueInBST(node):
    temp=node
    while temp.left:
        temp=temp.left
    return temp.data
def MaximumValueInBST(node):
    temp=node
    while temp.right:
        temp=temp.right
    return temp.data
def searchValueInBST(node,key):
    if node == None:
        return False
    if node.data<key:
        return searchValueInBST(node.right,key)
    elif node.data>key:
        return searchValueInBST(node.left,key)
    else:
        return True
    
    return False
    
    
    

root=None
root=insertBST(root,23)
root=insertBST(root,233)
root=insertBST(root,243)
root=insertBST(root,234)
root=insertBST(root,2)
inoderTraversal(root)
print("Mininum value is ",MinimumValueInBST(root))
print("maximum value is in BST Tree",MaximumValueInBST(root))
if searchValueInBST(root,243)==True:
    print(" Value is found")
else:
    print("value is not found in tree")

