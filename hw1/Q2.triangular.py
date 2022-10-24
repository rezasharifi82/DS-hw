#In The Name Of God
m=int(input())
ai=[]
for i in range(m):
    ai.append(list(map(int,input().split())))
upper_count=0
downer_count=0
con=m*(m-1)*0.5
for i in range(m):
    for j in range(i+1,m):
        if(ai[i][j]==0):
            downer_count+=1
        elif(ai[j][i]==0):
            upper_count+=1
if(upper_count==con and downer_count==con):
    print("diagonal")
elif(upper_count==con):
    print("upper triangular")
elif(downer_count==con):
    print("downer triangular")
else:
    print("nothing!")    
