# definiuje stos pusty
# zadeklaruj 2 zmienne jeedna boolowska zakładająca że stos jest poprawny oraz zemienna indeks złurząca do przechodzienia elem listy
#
# dopuki ilość naszego elementu jest mniejsza od size
#
# jeśli znak jest nawiasem otwierającym dodaj znak na stos
# w przeciwnym wypadku ozxnacza to że nawias zamykajocy sprawdź czy st0s jest pusty "podstaw folsa"

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

a='())(()))'
tab = list(a)
s= Stack()
l=len(a)
i=0
b=0
c=0
print(tab)

while i<l:

    if tab[i]=='(':
        s.push(tab[i])
        # print("otwierający w ineksie", i)
        # c=c+1
        # DO DOKOŃCZENIA INDEKSOWANIE "(" NAWIASÓW
    else:
        if s.isEmpty():
            print("zamykajacy w ineksie",i)
            b=b+1
        else:
            s.pop()
    i+=1
if b==0:
    if s.isEmpty():
        print("wszystko dobrze")
    else:
        print("brakuje otwierających ", s.size())
else:
    print("za durzo zamykajacych ",b)



# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# s.push('34')
# print(s.isEmpty())
# print(s.size())
# s.pop()
# print(s.size())
# print(s.peek())