from collections import deque
def bfs(graph,start,end,weight):
    visited=[False]*(len(graph)+1)
    queue=deque()
    queue.append(start)
    visited[start]=True

    while queue:
        vertex=queue.popleft()
        for adj_vertex,adj_weight in graph[vertex]:
            if not visited[adj_vertex] and adj_weight>=weight:
                visited[adj_vertex]=True
                queue.append(adj_vertex)

    return visited[end]

def solution():
    n_vertex,n_edge=list(map(int,input().split(' ')))
    graph=[[] for _ in range(0,n_vertex+1)]
    min_weight,max_weight=1000000000,1

    for _ in range(n_edge):
        start,end,weight=list(map(int,input().split(' ')))
        graph[start].append((end,weight))
        graph[end].append((start,weight))
        min_weight=min(min_weight,weight)
        max_weight=max(max_weight,weight)

    start_vertex,end_vertex=list(map(int,input().split(' ')))

    result=0

    while min_weight<=max_weight:
        med=(min_weight+max_weight)//2
        if bfs(graph,start_vertex,end_vertex,med):
            result=med
            min_weight=med+1
        else:
            max_weight=med-1
    print(result)

if __name__ == "__main__":
    solution()
