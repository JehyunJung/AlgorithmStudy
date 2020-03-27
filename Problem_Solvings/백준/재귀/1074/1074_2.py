def solve(n,x,y,x_pos,y_pos,result):
    if n==2:
        if x==x_pos and y==y_pos:
            print(result)
            return result
        result+=1
        if x==x_pos and y+1 ==y_pos:
            print(result)
            return result
        result+=1
        if x==x_pos+1 and y==y_pos:
            print(result)
            return result
        result+=1
        if x+1==x_pos and y+1 ==y_pos:
            print(result)
            return result
        result+=1
        return result

    result=solve(n/2,x,y,x_pos,y_pos,result)
    result=solve(n/2,x+n/2,y,x_pos,y_pos,result)
    result=solve(n/2,x,y+n/2,x_pos,y_pos,result)
    result=solve(n/2,x+n/2,y+n/2,x_pos,y_pos,result)

def solution():
    result=0
    space,y_pos,x_pos=list(map(int, input().split(' ')))
    solve(2**space,0,0,x_pos,y_pos,result)

if __name__ == "__main__":
    solution()
