def solution():
    num=int(input())
    datas=[]
    for _ in range(num):
        datas.append(int(input()))
    datas.sort()
    sum=0
    for i in range(0,len(datas)):
        sum+=abs((i+1)-datas[i])
    print(sum)
if __name__== "__main__":
    solution()