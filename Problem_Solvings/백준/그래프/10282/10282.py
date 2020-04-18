import heapq
def dijkstra(graph,n_vertex,start):
    distances=[float('inf')]*(n_vertex+1)
    distances[start]=0
    heap=[]

    heapq.heappush(heap,(0,start))

    while heap:
        vertex_weight,vertex=heapq.heappop(heap)
        for adjacent_vertex,weight in graph[vertex]:
            if distances[vertex] + weight < distances[adjacent_vertex]:
                distances[adjacent_vertex]=distances[vertex] + weight
                heapq.heappush(heap,(distances[adjacent_vertex],adjacent_vertex))

    return distances
def solution():
    n_testcases=int(input())

    for _ in range(n_testcases):
        n_vertex, n_edges,start_point=map(int,input().split(' '))
        graph=[[] for _ in range(n_vertex+1)]

        for _ in range(n_edges):
            end,start,weight=map(int,input().split(' '))
            graph[start].append((end,weight))

        distances=dijkstra(graph,n_vertex,start_point)
        max_distance=0
        victim_count=0
        for distance in distances:
            if distance == float('inf'):
                continue
            max_distance=max(max_distance,distance)
            victim_count+=1
        print(victim_count,max_distance)

if __name__=="__main__":
    solution()