# INSERTION INT0 BINARY SEARCH TREE

class TreeNode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None

def printinorder(root):
    if root == None:
        return
    printinorder(root.left)
    print(root.val,end = ", ")
    printinorder(root.right)

def insertIntoBST(root,val):
    if root == None:
        return TreeNode(val)
    elif root.val > val:
        root.left = insertIntoBST(root.left,val)
    else:
        root.right = insertIntoBST(root.right,val)
    return root
    
nums = [10, 8, 12, 5, 23, 20]
root = None
for ele in nums:
    root = insertIntoBST(root,ele)
printinorder(root)