
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





str= '7 3 + 5 2 - 2 ^ * ='
str2=str.split(' ')
print(str2)
s= Stack()
l=len(str2)
i=0
b=0

print("tak wygląda dzialanie ", str)

for i in range(l):
    if '+'==str2[i]:
        x=s.pop()
        y=s.pop()
        s.push(y+x)
        
    elif '-'==str2[i]:
        x=s.pop()
        y=s.pop()
        s.push(y-x)
    elif '*'==str2[i]:
        x=s.pop()
        y=s.pop()
        s.push(y*x)

    elif '/'==str2[i]:
        x=s.pop()
        y=s.pop()
        s.push(y/x)

    elif '^'==str2[i]:
        x=s.pop()
        y=s.pop()
        s.push(y**x)
    elif '='==str2[i]:
        print("wynik", s.peek())

    else:
        s.push(int(str2[i]))




# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# s.push('34')
# print(s.isEmpty())
# print(s.size())
# s.pop()
# print(s.size())
# print(s.peek())