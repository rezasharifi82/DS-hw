#In The Name Of God
def sparse_product(a:list , b:list):
    a0=a[0]
    b0=b[0]
    if(a0[1]!=b0[0]):
        print("Invalid Case!")
    else:
        # c=a0[0]*b0[1]
        # conj=++
        c=[[a0[0],b0[1],0]]
        for i in range(1,len(a)):
            for j in range(1,len(b)):
                if(a[i][0]==b[j][0] and a[i][1]==b[j][1]):
                    c.append([i-1,j-1,a[i][-1]*b[j][-1]])
                    c[0][-1]+=1

        print(*c,sep="\n")

a=[ [4,5,4],
    [0,2,3],
    [0,4,4],
    [1,3,7],
    [3,2,6]
]
b=[ [5,3,3],
    [0,2,2],
    [0,1,5],
    [3,1,4]
]
# print(a[-1])
sparse_product(a,b)

    
