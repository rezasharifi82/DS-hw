#In The Name Of God
def sparse_product(a:list , b:list):
    a0=a[0]
    b0=b[0]
    if(a0[1]!=b0[0]):
        print("Invalid Case!")
    else:
        # c=a0[0]*b0[1]
        # conj=++
        c=[[0 for i in range(b0[1])] for j in range(a0[0])]

        for i in range(1,len(a)):
            for j in range(1,len(b)):
                if(a[i][1]==b[j][0]):
                    c[a[i][0]][b[j][1]]+=(a[i][-1]*b[j][-1])

        print(*c,sep="\n")

a=[ [3,4,7],
    [0,0,4],
    [0,1,2],
    [1,0,1],
    [1,2,2],
    [1,3,1],
    [2,0,2],
    [2,3,2]
]
b=[ [4,2,5],
    [0,0,1],
    [1,0,2],
    [2,0,3],
    [2,1,1],
    [3,1,1]
]
sparse_product(a,b)
#Output:  absolutely it's not sparse
# 8 0
# 7 3
# 2 2
