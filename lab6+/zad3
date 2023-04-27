class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return  self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

str=')}]{(['
s= Stack()
l=len(str)
i=0
b=0

# można by zrobić to na mniejszej ilość linijek ale nie jest wymagana mała ilość linijek
print(str)

while i<l:

    if str[i]=='(':
        s.push(str[i])
    else:
        if s.isEmpty() and str[i]==')':
            # print("zamykajacy w ineksie",i)
            b=b+1
        elif str[i]==')':
            s.pop()
        else:
            pass
    i+=1

if s.size()>0 and b>0:
    print("złe ustawienie 'końcowych' nawiasów: )(")
    
if b==0 and s.isEmpty(): 
        print("wszystko dobrze ()")

if s.size()>0:
    print("za durzo otwierających ( ", s.size())
if b>0:
    print("za durzo zamykajacych ) ",b)

print()

i=0
b=0
s.__init__()


while i<l:

    if str[i]=='[':
        s.push(str[i])
    else:
        if s.isEmpty() and str[i]==']':
            # print("zamykajacy w ineksie",i)
            b=b+1
        elif str[i]==']':
            s.pop()
        else:
            pass
    i+=1

if s.size()>0 and b>0:
    print("złe ustawienie 'końcowych' nawiasów: ][")
    
if b==0:
    if s.isEmpty():
        print("wszystko dobrze []")
    else:
       print("za durzo otwierających [ ", s.size())
else:
        print("za durzo zamykajacych ] ",b)


print()

i=0
b=0
s.__init__()


while i<l:

    if str[i]=='{':
        s.push(str[i])
    else:
        if s.isEmpty() and str[i]=='}':
            # print("zamykajacy w ineksie",i)
            b=b+1
        elif str[i]=='}':
            s.pop()
        else:
            pass
    i+=1

if s.size()>0 and b>0:
    print("złe ustawienie 'końcowych' nawiasów: }{")
    
if b==0:
    if s.isEmpty():
        print("wszystko dobrze {}")
    else:
       print("za durzo otwierających { ", s.size())
else:
        print("za durzo zamykajacych } ",b)


# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# s.push('34')
# print(s.isEmpty())
# print(s.size())
# s.pop()
# print(s.size())
# print(s.peek())