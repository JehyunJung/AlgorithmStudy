def simpleUnion(parent,child,i,j):
    i_root=i
    while i_root!=parent[i_root]:
        i_root=parent[i_root]

    while i!=i_root:
        s=parent[i]
        parent[i]=i_root
        i=s

    j_root=j
    while j_root!=parent[j_root]:
        j_root=parent[j_root]

    while j!=j_root:
        s=parent[j]
        parent[j]=j_root
        j=s

    if (i_root!=j_root):
        parent[i_root]=j_root
        child[j_root]+=child[i_root]


def solution(test_cases):
    for i in range(test_cases):
        friend_num=int(input())
        parent=dict()
        child=dict()
        for j in range(friend_num):
            friend1,friend2=list(input().split(' '))
            if friend1 not in parent:
                parent[friend1]=friend1
                child[friend1]=1
            if friend2 not in parent:
                parent[friend2]=friend2
                child[friend2]=1

            simpleUnion(parent,child,friend1,friend2)
            friend1_root=friend1
            while friend1_root!=parent[friend1_root]:
                friend1_root=parent[friend1_root]

            while friend1!=friend1_root:
                s=parent[friend1]
                parent[friend1]=friend1_root
                friend1=s

            print(child[friend1_root])



if __name__ == "__main__":
    test_cases=int(input())
    solution(test_cases)
