#LEVEL ORDER TRAVERSAL


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printleveloredertraversal(root):
    if root == None:
        return
    Q=[root]
    result=[]
    while len(Q)>0:
        n=len(Q)
        subresult=[]
        for i in range(n):

            currNode=Q.pop(0)
            subresult.append(currNode.data)

            if currNode.left != None:
                Q.append(currNode.left)

            if currNode.right != None:
                Q.append(currNode.right)

        result.append(subresult)
    print(result)
obj1=Node(100)
obj2=Node(21)
obj3=Node(-151)
obj4=Node(87)
obj5=Node(12)
obj6=Node(52)
obj7=Node(8)
obj8=Node(27)
obj9=Node(28)
obj10=Node(7)

obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6
obj3.right=obj7
obj4.right=obj8
obj5.right=obj9
obj7.left=obj10
printleveloredertraversal(obj1)