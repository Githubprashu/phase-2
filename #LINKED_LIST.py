#LINKED LIST

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
obj1=Node(71)
obj2=Node(72)
obj3=Node(73)
obj4=Node(74)
obj5=Node(75)
obj6=Node(76)
obj7=Node(77)
obj8=Node(78)
obj9=Node(79)
obj10=Node(80)

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
    currentnode=currentnode.next