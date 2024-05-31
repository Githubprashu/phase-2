#DELETION NODE FRM BINARY SEARCH TREE


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

def deletedNodeFromBST(root,val):
    if root == None:
        return None
    elif root.val>val:
        root.left=deletedNodeFromBST(root.left,val)
    elif root.val<val:
        root.right=deletedNodeFromBST(root.right,val)
    else:
        if root.left==None and root.right==None:
            return None
        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        
        curr=root.right
        while curr.left != None:
            curr=curr.left
            
        root.val=curr.val
        root.right=deletedNodeFromBST(root.right,curr.val)
    return root

nums = [10, 8, 12, 5, 23, 20]
root = None
for ele in nums:
    root = insertIntoBST(root,ele)
printinorder(root)
print()
root=deletedNodeFromBST(root,20)
printinorder(root)