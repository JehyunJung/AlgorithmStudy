from collections import deque
def bfs(graph,visited,K,x,y):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    queue=deque([(x,y)])
    component=[(x,y)]
    N=len(graph)
    visited[x][y]=True
    while queue:
        curr_x,curr_y=queue.popleft()
        for dir in range(4):
            next_x,next_y=curr_x+dx[dir],curr_y+dy[dir]
            if 0>next_x or next_x>N-1 or 0>next_y or next_y >9:
                continue
            elif visited[next_x][next_y]:
                continue
            elif graph[curr_x][curr_y]!=0 and graph[next_x][next_y]==graph[curr_x][curr_y]:
                queue.append((next_x,next_y))
                component.append((next_x,next_y))
                visited[next_x][next_y]=True

    if len(component) >=K:
        for x,y in component:
            graph[x][y]=0
        return True

    return False

def puller(graph):
    N=len(graph)
    for y in range(10):
        non_zeros=[]
        for x in range(N):
            if graph[x][y]!=0:
                non_zeros.append(graph[x][y])
        non_zero_len=len(non_zeros)
        for index in range(N-non_zero_len):
            graph[index][y]=0

        for index in range(N-non_zero_len,N):
            graph[index][y]=non_zeros[index-N+non_zero_len]




def solution():
    graph_size,K=map(int,input().split())
    graph=[[0 for _ in range(10)] for _ in range(graph_size)]
    mapping='0123456789'
    for x in range(graph_size):
        str=input()
        for y in range(10):
            graph[x][y]=mapping.index(str[y])


    while True:
        visited=[[False for _ in range(10)] for _ in range(graph_size)]
        finish_flag=True
        for x in range(graph_size):
            for y in range(10):
                if graph[x][y]==0:
                    visited[x][y]=True
                    continue
                if bfs(graph,visited,K,x,y):
                    finish_flag=False

        if finish_flag==True:
            break
        puller(graph)

    for x in range(graph_size):
        for y in range(10):
            print(graph[x][y],end="")
        print()


if __name__== "__main__":
    solution()