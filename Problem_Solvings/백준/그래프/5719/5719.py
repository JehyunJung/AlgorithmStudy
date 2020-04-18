import heapq
from collections import deque
def dijkstra(graph,n_vertex,start,min_path):
    distances=[float('inf')]*(n_vertex)
    path=[-1]*(n_vertex)
    distances[start]=0
    heap=[]

    heapq.heappush(heap,(0,start))
    while heap:
        vertex_weight,vertex=heapq.heappop(heap)
        for adjacent_vertex,weight in graph[vertex] :
            if distances[vertex] + weight < distances[adjacent_vertex] and not min_path[vertex][adjacent_vertex]:
                distances[adjacent_vertex]=distances[vertex] + weight
                path[adjacent_vertex]=vertex
                heapq.heappush(heap,(distances[adjacent_vertex],adjacent_vertex))

    return path,distances


def bfs(graph,distances,start,min_path):
    queue=deque([start])
    while queue:
        vertex=queue.popleft()
        for adjacent_vertex, weight in graph[vertex]:
            #최단 경로 중의 간선
            if distances[adjacent_vertex]+weight == distances[vertex]:
                min_path[adjacent_vertex][vertex]=True
                queue.append(adjacent_vertex)

def solution():
    while True:
        n_vertex, n_edges=map(int,input().split(' '))
        if n_vertex==0 and n_edges ==0:
            return

        start_point,end_point=map(int,input().split(' '))
        graph=[[] for _ in range(n_vertex)]
        reverse_graph=[[] for _ in range(n_vertex)]

        for _ in range(n_edges):
            start,end,weight=map(int,input().split(' '))
            graph[start].append((end,weight))
            reverse_graph[end].append((start,weight))
        min_path=[[False]*(n_vertex) for _ in range(n_vertex)]

        path,distances=dijkstra(graph,n_vertex,start_point,min_path)
        bfs(reverse_graph,distances,end_point,min_path)
        path,sub_distances=dijkstra(graph,n_vertex,start_point,min_path)

        if sub_distances[end_point] != float('inf'):
            print(sub_distances[end_point])
        else:
            print(-1)

if __name__=="__main__":
    solution()