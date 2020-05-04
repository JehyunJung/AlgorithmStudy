def bfs(current_row,current_col):
    q=set()
    q.add((current_row,current_col,arrays[current_row][current_col]))
    global max_distance
    max_distance=1
    while q:
        current_row,current_col,path=q.pop()
        max_distance=max(len(path),max_distance)
        for dir in range(4):
            next_row,next_col=current_row+row_move[dir],current_col+col_move[dir]
            if 0<=next_row<n_rows and 0<=next_col<n_cols:
                if arrays[next_row][next_col] not in path:
                    q.add((next_row,next_col,path+arrays[next_row][next_col]))

n_rows, n_cols=map(int,input().split(' '))
arrays=[]
for _ in range(n_rows):
    arrays.append(input())

row_move=[-1,0,1,0]
col_move=[0,1,0,-1]

bfs(0,0)
print(max_distance)