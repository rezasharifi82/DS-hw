#In The Name Of God
from collections import deque
def iinsert(b:deque,i):
    c=deque()
    while(len(b)>0):
        d=b.popleft()
        if(i>d):
            c.append(d)
        else:
            b.appendleft(d)
            b.appendleft(i)
            c.extend(b)
            b=c.copy()
            break
    else:
        b.append(i)
    return b
a=[-1,2,2,0,88,1,4,8,9,6,66,9,5,2,6,6,99,0,-2]
a=deque(a)
b=deque()
while(len(a)>0):
    c=a.pop()
    b=iinsert(b,c)
b=list(b)
print(b)

    




