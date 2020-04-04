def preOrder(root):
    print(root.data,end='')
    if root.left:
        preOrder(tree[root.left])
    if root.right:
        preOrder(tree[root.right])
def inOrder(root):
    if root.left:
        inOrder(tree[root.left])
    print(root.data,end='')
    if root.right:
        inOrder(tree[root.right])

def postOrder(root):
    if root.left:
        postOrder(tree[root.left])
    if root.right:
        postOrder(tree[root.right])
    print(root.data,end='')

class Node:
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right

def solution():
    num=int(input())
    global tree
    tree={}
    for _ in range(num):
        data,left,right=input().split(' ')
        if left == '.':
            left=None
        if right=='.':
            right=None
        tree[data]=Node(data,left,right)

    preOrder(tree['A'])
    print()
    inOrder(tree['A'])
    print()
    postOrder(tree['A'])

if __name__ =="__main__":
    solution()