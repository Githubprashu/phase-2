# 3 types of insertion codes

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printlinkedlist(head):
    currentNode=head
    while currentNode!= None:
        print(currentNode.data,end = "-->")
        currentNode=currentNode.next
print()

def insertattail(head,ele):
    temp=Node(ele)
    if head==None:
        return temp
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=temp
    return head
#task-1
def insertathead(head,ele):
    temp=Node(ele)
    temp.next=head
    return temp
#task-2
def insertatspecificposition(head,position,ele):
    if position==0:
        return insertathead(head,ele)
    
    temp=Node(ele)
    index=0
    currentNode=head

    while index!=position-1:
        currentNode=currentNode.next
        index+=1

    nextNode=currentNode.next
    temp.next=nextNode
    currentNode.next = temp 
    return head

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertattail(head, ele)
print("Final linked list is:")
printlinkedlist(head)
 
head =insertatspecificposition(head, 3, 101)
printlinkedlist(head)"""


"""def deleteTailNode(head):  
    if head==None or head.next==None:
        return None
    previous=None
    currentNode=head
    while currentNode.next!=None:
        pervious=currentNode
        currentNode=currentNode.next
    previous.next=None
    return head