class Node:
    def __init__(self):
        self.parent=None
        self.data=None
        self.left=None
        self.right=None

def inOrder(root,level):
    global count,height
    height=max(level,height)
    if root.left:
        count=inOrder(tree[root.left],level+1)
    count+=1
    level_min[level]=min(level_min[level],count)
    level_max[level]=max(level_max[level],count)
    if root.right:
        count=inOrder(tree[root.right],level+1)
    return count

num=int(input())

tree={index: Node() for index in range(1,num+1)}
for _ in range(num):
    data,left,right=map(int,input().split(' '))
    tree[data].data=data
    if left != -1:
        tree[data].left=left
        tree[left].parent=data
    if right != -1:
        tree[data].right=right
        tree[right].parent=data

root=-1
for i in range(1,num):
    if tree[i].parent ==None:
        root=i
        break
level_min=[num]*(num+1)
level_max=[0]*(num+1)
count=0
height=1

inOrder(tree[root],1)
max_level,max_width=1,(level_max[1]-level_min[1]+1)

for level in range(2,height+1):
    width=level_max[level]-level_min[level]+1
    if width>max_width:
        max_width=width
        max_level=level

print(max_level,max_width)

