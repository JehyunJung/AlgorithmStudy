def collapseFind(root):
    if root!=parent[root]:
        parent[root]=collapseFind(parent[root])
    return parent[root]

def simpleUnion(i,j):
    if (i!=j):
        parent[i]=j
        child[j]+=child[i]


def solution():
    test_cases=int(input())
    for i in range(test_cases):
        friend_num=int(input())
        global parent
        parent=dict()
        global child
        child=dict()
        for j in range(friend_num):
            friend1,friend2=list(input().split(' '))
            if friend1 not in parent:
                parent[friend1]=friend1
                child[friend1]=1
            if friend2 not in parent:
                parent[friend2]=friend2
                child[friend2]=1

            simpleUnion(collapseFind(friend1),collapseFind(friend2))
            print(child[collapseFind(friend1)])



if __name__ == "__main__":
    solution()
