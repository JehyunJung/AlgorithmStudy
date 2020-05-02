def collapseFind(parent,a):
    if parent[a]==a:
        return parent[a]
    parent[a]=collapseFind(parent,parent[a])
    return parent[a]

def simpleUnion(parent,a,b):
    parent[b]=a


def solution():
    n_elements=int(input())
    elements=[]
    parents=[n_elements]

    for i in range(1,n_elements+1):
        deadline,value=map(int,input().split(' '))
        elements.append((i,deadline,value))
        parents.append(i)

    value_sorted=sorted(elements,key=lambda x:x[2],reverse=True)
    scheduled=[0]*(n_elements+1)

    for (num,deadline,value) in value_sorted:
        index=collapseFind(parents,deadline)
        scheduled[index]=num
        prev_index=collapseFind(parents,index-1)
        simpleUnion(parents,prev_index,index)

    result=0
    for deadline in range(1,n_elements+1):
        task_num=scheduled[deadline]-1
        if elements[task_num][1]>=deadline:
            result+=elements[task_num][2]

    print(result)

if __name__=="__main__":
    solution()