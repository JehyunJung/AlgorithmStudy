from collections import deque
def bfs(graph,n_vertex,start_point):
    visited=[False]*(n_vertex+1)
    visited[start_point]=True

    queue=deque([start_point])
    while queue:
        vertex= queue.popleft()
        for adjacent_vertex in graph[vertex]:
            if not visited[adjacent_vertex]:
                queue.append(adjacent_vertex)
                visited[adjacent_vertex]=True
    return sum(visited)

def solution():
    n_vertex,n_edges=map(int,input().split(' '))
    graph=[[] for vertex in range(n_vertex+1)]

    for _ in range(n_edges):
        end,start=map(int,input().split(' '))
        graph[start].append(end)

    max_component=0
    candidates=[]
    for vertex in range(1, n_vertex+1):
        vertex_component=bfs(graph,n_vertex,vertex)
        max_component=max(vertex_component,max_component)
        candidates.append((vertex,vertex_component))

    results=[]
    for vertex,component_count in candidates:
        if component_count==max_component:
            results.append(vertex)

    for vertex in results:
        print(vertex,end=' ')


if __name__=="__main__":
    solution()