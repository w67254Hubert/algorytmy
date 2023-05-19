# lilista jdnokierunkowa

class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None

    def getdata(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data=newdata

    def setNext(self,newnext):
        self.next=newnext

temp=Node(93)
print(temp.getdata())
print(temp.getNext())


class unOrderdList:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head==None

    def add(self,item):
        temp= Node(item)
        temp.setNext(self.head)
        self.head=temp

    def size(self):
        current= self.head
        count=0
        while current != None:
            count= count+1
            current = current.getNext()
        return count

    def seartch(self,item):
        current=self.head
        found=False
        while current != None and not found:
            if current.getdata() == item:
                found=True
            else:
                current=current.getNext()
        return found


    def remoe(self,item):
        current=self.head
        previous= None
        found=False
        while not found:
            if current.getdata()==item:
                found=True
            else:
                previous=current
                current=current.getNext()
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())

mylist=unOrderdList()
mylist.add(12)
mylist.add(1)
mylist.add(23)
mylist.add(32)

print(mylist.size())
print(mylist.seartch(0))
print(mylist.seartch(123))


