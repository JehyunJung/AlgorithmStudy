def solution():
    bird_num=int(input())
    k=1
    count=0
    while bird_num>0:
        if k<=bird_num:
            count+=1
            bird_num-=k
            k+=1
        else:
            k=1
    print(count)

if __name__ == "__main__":
    solution()