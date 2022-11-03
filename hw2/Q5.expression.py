#In The Name Of God
from collections import deque
op=deque()
num=deque()
so=[]
s=input().strip()
k=int(s[0])
k=0
for i in s:
    if i in ["*","+","-","/"]:
        so.append(int(k))
        k=0
        so.append(i)
    else:
        k=k*10 +(int(i))
so.append(k)
j=0
p=0
for i in so:
    if(i in ["+","-"]):
        op.append(i)
    elif(i in ["/","*"]):
        j=num.pop()
        p=i
    else:
        if(p=="*"):
            num.append(j*i)
        elif(p=="/"):
            num.append(j//i)
        else:
            num.append(i)
        p=0
        j=0
while(len(num)>1):
    i=num.popleft()
    j=op.popleft()
    if(j=="+"):
        num.appendleft(i+num.popleft())
    elif(j=="-"):
        num.appendleft(i-num.popleft())
print(num.pop())

# 3+3*4+3*2-1*8/4
