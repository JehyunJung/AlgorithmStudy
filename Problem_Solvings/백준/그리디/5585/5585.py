def solution():
    remaining=1000-int(input())
    count=0
    for change in [500,100,50,10,5,1]:
        count += (remaining//change)
        remaining%=change
    print(count)
if __name__=="__main__":
    solution()