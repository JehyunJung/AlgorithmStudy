def solution():
    n=int(input())
    count=[1]*(n+1)
    count[1]=1

    for index in range(2,n+1):
        count[index]=(count[index-1]+count[index-2])%15746

    print(count[n])

if __name__=="__main__":
    solution()