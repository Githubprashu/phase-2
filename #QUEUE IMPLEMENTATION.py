#QUEUE IMPLEMENTATION

def enQueue(Q,ele):
    Q.append(ele)
    print(ele,"inserted into Queue")

def deQueue(Q):
    if len(Q)==0:
        print("Queue is empty")
        return
    print(Q[0],"is getting deleted")
    Q.pop(0)

Q=[]
enQueue(Q,10)
enQueue(Q,20)
enQueue(Q,30)
enQueue(Q,40)
enQueue(Q,50)

deQueue(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)

