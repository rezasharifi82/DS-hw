#In The Name Of God
def transpose(a:list):
    b=a[1:]
    b.sort(key= lambda x: x[1])
    for i in b:
        i[0],i[1]=i[1],i[0]

    print(*b , sep='\n')

a=[[6,6,8],
   [1,1,5],
   [1,4,10],
   [1,6,-5],
   [2,2,12],
   [2,3,4],
   [3,4,-8],
   [5,1,10],
   [6,3,45] 
    ]
transpose(a)
#Output:
# [1, 1, 5]
# [1, 5, 10]
# [2, 2, 12]
# [3, 2, 4]
# [3, 6, 45]
# [4, 1, 10]
# [4, 3, -8]
# [6, 1, -5]
