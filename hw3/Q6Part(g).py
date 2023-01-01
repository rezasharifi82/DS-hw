# This code absolutely not complete!
# We need some fundamental structures that is not implemented here.


def insert(root,data):
    if(root==None):
        root=data
    elif(root.key<data.key):
        if(root.left==None):
            root.left=data
        else:
            insert(root.left,data)
    else:
        if(root.right==None):
            root.right=data
        else:
            insert(root.right,data)
