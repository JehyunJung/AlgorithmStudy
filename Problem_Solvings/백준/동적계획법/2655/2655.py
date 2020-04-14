def solution():
    n_blocks=int(input())
    blocks=[]
    blocks.append((0,0,0,0))
    for i in range(1,n_blocks+1):
        width,height,weight=map(int,input().split(' '))
        blocks.append((i,width,height,weight))

    blocks.sort(key=lambda x:x[3])

    tower=[0]*(n_blocks+1)

    for i in range(1,n_blocks+1):
        max_height=tower[i]
        for j in range(0,i):
            if blocks[i][1]>blocks[j][1]:
                max_height=max(max_height,tower[j])
        tower[i]=max_height+blocks[i][2]
    max_value=max(tower)
    index=n_blocks
    result=[]
    while index!=0:
        if tower[index]==max_value:
            result.append(blocks[index][0])
            max_value-=blocks[index][2]
        index-=1

    print(len(result))
    result.reverse()
    for block in result:
        print(block)
if __name__=="__main__":
    solution()