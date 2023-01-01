#In The Name Of God
#All about the Binary Tree

from collections import deque


class Node:
    def __init__(self,data=None) -> None:
        self.left=None
        self.data=data
        self.right=None
        self.parent=None
class BT:
    def __init__(self,root:Node) -> None:
        self.root=root
        self.app=deque()
        root.left=Node()
        root.right=Node()
        self.app.append(root.left)
        self.app.append(root.right)
        root.left.parent=root
        root.right.parent=root
    def insert(self,data):
        q=self.app.popleft()
        q.data=data
        q.left=Node()
        q.right=Node()
        self.app.append(q.left)
        self.app.append(q.right)
        q.left.parent=q
        q.right.parent=q
    @staticmethod
    def return_inorder(root:Node):
        if(root.data==None):
            return []
        else:
            l=BT.return_inorder(root.left)
            v=root.data
            r=BT.return_inorder(root.right)
            l.append(v)
            l.extend(r)
            return l
        




class dll:
    def __init__(self,head:Node) -> None:
        self.head=head
        self.last=head
    def insert(self,data):
        node=Node(data)
        self.last.right=node
        node.left=self.last
        self.last=self.last.right
    def __str__(self) -> str:
        p=self.head
        a=[]
        while(p.right!=None):
            a.append(p.data)
            p=p.right
        
        return str(a)




'''
          1
       /    \
      2      3
     / \    / \
    4   5  6   7


'''
root=Node(1)
my_tree=BT(root)
a=range(2,8)
for i in a:
    my_tree.insert(i)


    
k=BT.return_inorder(my_tree.root)
the_doubly_linked_list=dll(Node(k[0]))
for i in k[1:]:
    the_doubly_linked_list.insert(i)

print(the_doubly_linked_list)
