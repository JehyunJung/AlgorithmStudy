from collections import deque
def bfs(graph,n_vertex):
    visited=[False]*(n_vertex+1)
    visited[1]=True

    queue=deque([1])
    while queue:
        vertex=queue.popleft()
        for adjacent_vertex in graph[vertex]:
            if not visited[adjacent_vertex]:
                queue.append(adjacent_vertex)
                visited[adjacent_vertex]=True

    return visited

def solution():
    n_vertex=int(input())
    n_edges=int(input())

    graph =[[] for _ in range(n_vertex+1)]
    for _ in range(n_edges):
        start,end=map(int,input().split(' '))
        graph[start].append(end)
        graph[end].append(start)
    visited=bfs(graph,n_vertex)
    print(sum(visited)-1) #the sum of visited means number of visited vertex because True value represents 1 and minus 1 means excepting the starting vertex
if __name__=="__main__":
    solution()