def solve(n,x,y):
    global result
    if n==2:
        if x==x_pos and y==y_pos:
            print(result)
            return
        result+=1
        if x==x_pos and y+1 ==y_pos:
            print(result)
            return
        result+=1
        if x==x_pos+1 and y==y_pos:
            print(result)
            return
        result+=1
        if x+1==x_pos and y+1 ==y_pos:
            print(result)
            return
        result+=1
        return

    solve(n/2,x,y)
    solve(n/2,x+n/2,y)
    solve(n/2,x,y+n/2)
    solve(n/2,x+n/2,y+n/2)

if __name__ == "__main__":
    result=0
    space,y_pos,x_pos=list(map(int, input().split(' ')))
    solve(2**space,0,0)