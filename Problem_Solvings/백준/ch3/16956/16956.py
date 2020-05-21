def solution():
    row,column=map(int,input().split(' '))
    pos_map=[list(input()) for _ in range(row)]
    dx=[0,1,0,-1]
    dy=[-1,0,1,0]

    check=False
    for i in range(row):
        for j in range(column):
            if pos_map[i][j]=="W":
                for dir in range(4):
                    next_x,next_y = i+dx[dir],j+dy[dir]
                    if 0<=next_x<column and 0<=next_y<row and pos_map[next_y][next_x]=="S":
                        check=True

    if check:
        print(0)
    else:
        print(1)
        for i in range(row):
            for j in range(column):
                if pos_map[i][j] == ".":
                    pos_map[i][j]='D'
                print(pos_map[i][j],end="")
            print()







if __name__ =="__main__":
    solution()