##class 
"""class Student:
    def __init__(self,name,rollnum,javamarks,pythonmarks,mathsmarks):
        self.name=name
        self.rollnum=rollnum
        self.javamarks=javamarks
        self.pythonmarks=pythonmarks
        self.mathsmarks=mathsmarks
obj=Student("hari","21a",80,90,67)
print(obj.name)
print(obj.rollnum)
print(obj.javamarks)
print(obj.pythonmarks)
print(obj.mathsmarks)  
obj1=Student("madhu","21d",78,90,90)
print(obj1.name)
print(obj1.rollnum)
print(obj1.javamarks)
print(obj1.pythonmarks)
print(obj1.mathsmarks) 
obj2=Student("prasanth","21f",87,32,54)
print(obj2.name)
print(obj2.rollnum)
print(obj2.javamarks)
print(obj2.pythonmarks)
print(obj2.mathsmarks)"""


##limkedlist      
"""class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
obj1=Node(10)
obj2=Node(20)
obj3=Node(30)
obj4=Node(40)
obj5=Node(50)
obj6=Node(60)
obj7=Node(70)
obj8=Node(80)
obj9=Node(90)
obj10=Node(100)

obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=obj5
obj5.next=obj6
obj6.next=obj7
obj7.next=obj8
obj8.next=obj9
obj9.next=obj10

currentnode=obj1
while currentnode !=None:
    print(currentnode.data)
    currentnode=currentnode.next"""

##inseration at tail position

"""class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
def printLinkedList(head):
    currentNode = head 
    while currentNode != None:
        print(currentNode.data, end = " --> ")
        currentNode = currentNode.next
    print()
 
def insertAtTail(head, ele):
    temp = Node(ele)
    if head == None:
        return temp
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp 
    return head
 
 
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertAtTail(head, ele)
    printLinkedList(head)
print("Final linked list is:")
printLinkedList(head)"""
 

 ## 3 type inseration code
     

"""class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
def printLinkedList(head):
    currentNode = head 
    while currentNode != None:
        print(currentNode.data, end = " --> ")
        currentNode = currentNode.next
    print()
 
def insertAtTail(head, ele):
    temp = Node(ele)
    if head == None:
        return temp
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp 
    return head
 
# Task - 1
def insertAtHead(head, ele):
    temp = Node(ele)
    temp.next = head 
    return temp
 
# Task - 2
def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return insertAtHead(head, ele)
 
    temp = Node(ele)
    index = 0 
    currentNode = head 
 
    while index != position - 1:
        currentNode = currentNode.next 
        index += 1 
 
    nextNode = currentNode.next 
    temp.next = nextNode 
    currentNode.next = temp 
    return head
 
 
 
 
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertAtTail(head, ele)
print("Final linked list is:")
printLinkedList(head)
 
head =insertAtSpecificPosition(head, 3, 101)
printLinkedList(head)"""

"""def deletetailnode(head):
    if head==None or head.next==None:
        return None
    previous=None
    currentnode=head
    while currentnode.next !=None:
        previous=currentnode
        currentnode= currentnode.next
    previous.next=None
    return head """ 

##stack implementation

"""def push(stack,ele):
    stack.append(ele)
    print(ele,"inserteed into stack successfully")
def pop(stack):
    if len(stack)==0:
        print("stack is empty")
        return
    print(stack[-1],"deleted successfully")
    stack.pop()
stack=[]
push(stack,10)
push(stack,20)
push(stack,30)
push(stack,40)
push(stack,50)"""


##queue implementataion


"""def enQuene(Q,ele):
    Q.append(ele)
    print(ele,"inserted into quene")
def deQueue(Q):
    if len(Q)==0:
        print("Queue is empty")
        return
    print(Q[0],"is getting deleted")
    Q.pop(0)

Q=[]
enQuene(Q,10)
enQuene(Q,20)
enQuene(Q,30)
enQuene(Q,40)
enQuene(Q,50)

deQueue(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)"""


"""def isBalanced(word):
    stack=[]
    for ele in word:
        if ele=='(':
            stack.append(ele)
        else:
            if len(stack)==0:
                return False
            else:
                stack.pop()
    if len(stack)==0:
        return True
    return False

word='(((((())))))'
result=isBalanced(word)
print(result)"""



"""class Solution(object):
    def isvaild(self,s):
        stack=[]
        openBrackets=["(","{","["]
        for ele in s:
            if ele in openBrrackets:
                stack.append(ele)
            else:
                if len(stack)==0:
                    return False
                elif ele==')':
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        return False
                elif ele==')':
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        return False
        if len(stack)==0:
            return True
        return False
s='{}()'
obj=Solution()"""

#LINEAR SEARCH

"""nums=[0,10,20,30,40,50]
target=40
flag=-1
n=len(nums)
for index in range(n):
    if nums[index]==target:
        flag=index
        break
if flag==-1:
    print("not found")
else:
    print("target found at:",flag)"""


#BINARY SEARCH

"""nums=[10,20,30,40,50]
target=20
nums=sorted(nums)

left=0
right=len(nums)-1
flag=-1

while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        flag=mid
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid+1
if flag==-1:
    print("target not found")
else:
    print("target found at index:",flag)
"""


#bubblesort

"""def performbubblesort(nums):
    n=len(nums)
    fixthisindex=n-1
    while fixthisindex>0:
        for index in range(fixthisindex):
            if nums[index]>nums[index+1]:
                temp=nums[index]
                nums[index]=nums[index+1]
                nums[index+1]=temp
        print(nums)
        fixthisindex-=1

nums=[10,8,2,14,12,7]
print("before sorting:",nums)

performbubblesort(nums)
print("after sorting:",nums)"""



##selectionsort

"""def performselectionsort(nums):
    n=len(nums)
    fixthisindex=n-1
    while fixthisindex>0:
        maxeleindex=fixthisindex
        for index in range(fixthisindex):
            if nums[index]>nums[maxeleindex]:
                maxeleindex=index
        if maxeleindex !=fixthisindex:
            temp=nums[maxeleindex]
            nums[maxeleindex]=nums[fixthisindex]
            nums[fixthisindex]=temp
        print(nums)
        fixthisindex-=1
nums=[22,7,90,78,35,11]
print("before sorting:",nums)

performselectionsort(nums)
print("after sorting:",nums)"""




#insertionsort

"""def performInsertionSort(nums):
    n = len(nums)
    lastEleInSortedArr = 0 
    for firstIndex in range(1, n):
        temp = nums[firstIndex]
        previous = lastEleInSortedArr 
 
        # [7, 9, 12, 34]
        while previous >= 0 and nums[previous] > temp:
            nums[previous + 1] = nums[previous]
            previous -= 1 
        nums[previous + 1] = temp 
        lastEleInSortedArr += 1
 
nums = [10, 8, 2, 14, 12, 7]
#nums = list(map(int, input().split()))
print("Before sorting:", nums)
 
performInsertionSort(nums)
 
print("After sorting:", nums)"""


#insertion into binary search tree

"""class Treenode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
def printinorder(root):
    if root==None:
        return
    printinorder(root.left)
    print(root.val,end=",")
    printinorder(root.right)        
def insertintobst(root,val):
    if root==None:
        return Treenode(val)
    elif root.val>val:
        root.left=insertintobst(root.left,val)
    else:
        root.right=insertintobst(root.right,val)
    return root      
nums=[10,8,12,5,23,20]
root=None
for ele in nums:
    root=insertintobst(root,ele)
printinorder(root)    """

#deletenodefrombst
"""class Treenode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
def printinorder(root):
    if root==None:
        return
    printinorder(root.left)
    print(root.val,end=",")
    printinorder(root.right)        
def insertintobst(root,val):
    if root==None:
        return Treenode(val)
    elif root.val>val:
        root.left=insertintobst(root.left,val)
    else:
        root.right=insertintobst(root.right,val)
    return root

def deletenodefrombst(root,val):
    if root ==None:
        return None
    elif root.val>val:
        root.left=deletenodefrombst(root.left,val)
    elif root.val<val:
        root.right=deletenodefrombst(root.right,val)
    else:
        if root.left==None and root.right==None:
            return None
        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        

        curr=root.right
        while curr.left !=None:
            curr=curr.left

        root.val=curr.val
        root.right=deletenodefrombst(root.right,curr.val)
    return root

nums=[10,8,12,5,23,20]
root=None
for ele in nums:
    root=insertintobst(root,ele)
printinorder(root)
print()
root=deletenodefrombst(root,20)
printinorder(root)""" 

#adjaceny matrix

n,m=map(int,input().split())
matrix=[]
for i in range(n):
    row=[0]*n
    matrix.append(row)
print(matrix)
for i in range(m):
    u,v=map(int,input().split())
    matrix[u][v]=1
    matrix[v][u]=1
print(matrix)         

        
            
      


    


        
      