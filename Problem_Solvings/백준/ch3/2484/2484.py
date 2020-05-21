from collections import Counter
def money_count():
    events=sorted(list(map(int,input().split(' '))))
    if len(set(events))==1:
        return 50000+5000*events[0]
    elif len(set(events))==2:
        if events[1]==events[2]:
            return 10000+1000*(events[1])
        else:
            return 2000+500*(events[1]+events[2])
    elif len(set(events))==3:
        for i in range(3):
            if events[i]==events[i+1]:
                return 1000+100*events[i]
    else:
        return 100*events[-1]

def solution():
    n_persons=int(input())
    print(max(money_count() for i in range(n_persons)))
if __name__=="__main__":
    solution()