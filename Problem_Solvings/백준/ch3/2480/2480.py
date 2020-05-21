def solution():
    events=sorted(list(map(int,input().split(' '))))

    if len(set(events))==1:
        print(10000+1000*events[0])
    elif len(set(events))==2:
        print(1000+100*events[1])
    else:
        print(100*events[2])


if __name__=="__main__":
    solution()