def solution():
    n_testcases=int(input())

    for _ in range(n_testcases):
        x1,y1,r1,x2,y2,r2=map(int,input().split(' '))
        if x1==x2 and y1==y2 and r1==r2:
            print(-1)
        else:
            distance=((x2-x1)**2+(y2-y1)**2)**(0.5)

            if distance > r1+r2 or distance<abs(r1-r2):
                print(0)
            elif distance==r1+r2 or distance==abs(r1-r2):
                print(1)
            elif distance<r1+r2:
                print(2)


if __name__=="__main__":
    solution()