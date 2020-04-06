import heapq
def solution():
    n_vertices, n_edges=list(map(int,input().split(' ')))
    graph={vertex: [] for vertex in range(1, n_vertices+1)}
    incoming_edges=[0]*(n_vertices+1)

    for _ in range(n_edges):
        start,end=list(map(int,input().split(' ')))
        incoming_edges[end]+=1
        graph[start].append(end)

    edge_heap=[vertex for vertex in range(1,n_vertices+1) if incoming_edges[vertex]==0]
    heapq.heapify(edge_heap)
    topological_order=[]
    while edge_heap:
        vertex=heapq.heappop(edge_heap)
        topological_order.append(vertex)
        for adjacent_vertex in graph[vertex]:
            incoming_edges[adjacent_vertex]-=1
            if incoming_edges[adjacent_vertex]==0:
                heapq.heappush(edge_heap,adjacent_vertex)

    for data in topological_order:
        print(data,end=' ')



if __name__ =="__main__":
    solution()