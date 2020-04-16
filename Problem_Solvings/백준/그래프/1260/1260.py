from collections import deque
def dfs(graph,start_point):
    visited=[False]*len(graph)
    visited[start_point]=True
    print(start_point,end=' ')
    for adjacent_vertex in graph[start_point]:
        if visited[adjacent_vertex]==False:
            dfs_iterate(graph,adjacent_vertex,visited)

    #Disconnected vertex 관리
    for vertex in range(len(graph)):
        if visited[vertex]==False and vertex!=0:
            dfs_iterate(graph,vertex,visited)


def dfs_iterate(graph,vertex,visited):
    visited[vertex]=True
    print(vertex,end=' ')
    for adjacent_vertex in graph[vertex]:
        if visited[adjacent_vertex]==False:
            dfs_iterate(graph,adjacent_vertex,visited)

def bfs(graph, start_point):
    visited=[False]*len(graph)
    visited[start_point]=True

    need_visit=deque()
    need_visit.append(start_point)

    while need_visit:
        vertex=need_visit.popleft()
        print(vertex,end=' ')
        for adjacent_vertex in graph[vertex]:
            if visited[adjacent_vertex]==False:
                need_visit.append(adjacent_vertex)
                visited[adjacent_vertex]=True

    #Disconnected vertex 관리
    for vertex in range(len(graph)):
        if visited[vertex]==False and vertex!=0:
            need_visit=deque([vertex])
    while need_visit:
        vertex=need_visit.popleft()
        print(vertex,end=' ')
        for adjacent_vertex in graph[vertex]:
            if visited[adjacent_vertex]==False:
                need_visit.append(adjacent_vertex)
                visited[adjacent_vertex]=True

def solution():
    n_vertex,n_edges,start_point=map(int,input().split(' '))
    graph=[[] for vertex in range(n_vertex+1)]

    for _ in range(n_edges):
        start,end=map(int,input().split(' '))
        graph[start].append(end)
        graph[end].append(start)
    [graph[vertex].sort() for vertex in range(n_vertex+1)]
    dfs(graph,start_point)
    print()
    bfs(graph,start_point)



if __name__ == "__main__":
    solution()