class student:
    def __init__(self,name,rollno,javamarks,pythonmarks,mathsmarks):
        self.name=name
        self.rollno=rollno
        self.javamarks=javamarks
        self.pythonmarks=pythonmarks
        self.mathsmarks=mathsmarks

    def printall(self):
        print(self.name)
        print(self.rollno)
        print(self.javamarks)
        print(self.pythonmarks)
        print(self.mathsmarks)


obj1=student("sridhar",120,80,70,60)
print(obj1.name)
print(obj1.rollno)
print(obj1.javamarks)
print(obj1.pythonmarks)
print(obj1.mathsmarks)

obj2=student("narendra",141,70,70,60)
print(obj2.name)
print(obj2.rollno)
print(obj2.javamarks)
print(obj2.pythonmarks)
print(obj2.mathsmarks)


obj3=student("raj",121,74,76,71)
print(obj3.name)
print(obj3.rollno)
print(obj3.javamarks)
print(obj3.pythonmarks)
print(obj3.mathsmarks)
    
obj=student("raj",121,74,76,71)
obj.printall()

obj=student("narendra",141,75,76,60)
obj.printall()