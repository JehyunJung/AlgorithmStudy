from collections import deque
def solution():
    test_cases=int(input())
    for _ in range(test_cases):
        n_cols,n_rows, n_vertex=map(int,input().split(' '))
        spaces=[]

        visited=[[False for _ in range(n_cols)] for _ in range(n_rows)]

        for _ in range(n_vertex):
            col,row=map(int,input().split(' '))
            spaces.append((row,col))

        n_component=0
        for row , col in spaces:
            if not visited[row][col]:
                queue=deque([(row,col)])
                while queue:
                    row,col=queue.popleft()
                    for next_row,next_col in (zip((row,row-1,row,row+1),(col-1,col,col+1,col))):
                        if  0<=next_row<n_rows and 0<=next_col<n_cols and not visited[next_row][next_col]:
                            if (next_row,next_col) in spaces:
                                queue.append((next_row,next_col))
                                visited[next_row][next_col]=True
                n_component+=1
        print(n_component)
if __name__ == "__main__":
    solution()