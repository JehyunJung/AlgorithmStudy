def solution():
    depth=int(input())
    numbers=[[0 for _ in range(depth+1)] for _ in range(depth+1)]
    sums=[[0 for _ in range(depth+1)] for _ in range(depth+1)]
    for i in range(1,depth+1):
        tmp=list(map(int,input().split(' ')))
        for j in range(1,i+1):
            numbers[i][j]=tmp[j-1]


    for i in range(1,depth+1):
        for j in range(1,i+1):
            sums[i][j]=numbers[i][j]+max(sums[i-1][j-1],sums[i-1][j])

    print(max(sums[-1]))
if __name__ == "__main__":
    solution()