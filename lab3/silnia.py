

def silnia(n):
    if n==0: return 1
    else: return n*silnia(n-1)

#wersja pierwsza nwdIteracyjne
def nwdIter(a,b):
    while a!=b:
        if a>b: a=a-b
        else: b=b-a
    return a


#wersja  rekurencyjnie
def nwdRek(a,b):
    if a!=b:
        if a>b: return nwdRek(a+b,b) #a=a-b
        else: return nwdRek(a,b-a) #b=b-a
    return a

print(nwdRek(12,18))

# 2 wersja iterowwan

def nwditerII(a,b):
    while b!=0:
        temp=b
        b=a%b
        a=temp
    return a

# 2 wersja rekurencyjnego

def nwdrekII(a,b):
    if b!=0:
        return nwdrekII(b,a%b)
    return a
#