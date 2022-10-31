#In The Name Of God
import re

a="</div>data<div>"
b="<div>data"
c="<div>data<div/>"
d="<div>data</div>"
s="<.+>.+</.+>"
#-------------------------------------
#regex solution

if(re.match(s,a)):
    print("yes")
else:
    print("no")

#-------------------------------------
#Stack solution
def check(s):
    c=0
    k=0
    d=-1
    for j,i in enumerate(s):
        if(i=="<"):
            k=j
            c+=1
        elif(i==">"):
            c-=1
    if(c==0 and s[k+1]=="/"):
        return True
    else:
        return False
        
        


        
    



print(check(a))
print(check(b))
print(check(c))
print(check(d))
        
            
        

        
# print(check(a))
