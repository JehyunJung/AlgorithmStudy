parents=dict()
childs=dict()

mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

def collapsing_find(parents,i):
    root=i
    while root!=parents[root]:
        root=parents[root]

    while i!=root:
        s=parents[i]
        parents[i]=root
        i=s
    return root

def collapsing_find2(i):
    if parents[i]!=i:
        parents[i]=collapsing_find2(parents[i])
    return parents[i]

def weightingUnion(parents,childs,i,j):
    if childs[i]>childs[j]:
        parents[i]=j
        childs[j]+=childs[i]
        if childs[j]== 0:
            childs[j]+=1
    else:
        parents[j]=i
        childs[i]+=childs[j]
        if childs[i]== 0:
            childs[i]+=1

def kruskal(graph):
    parents={vertex:vertex for vertex in graph['vertices']}
    childs={vertex:0 for vertex in graph['vertices']}
    edges=graph['edges']
    edges=sorted(edges,key=lambda x:x[0])

    total_weight=0
    vertices=list()
    MST=list()

    while set(vertices) != set(graph['vertices']):
        edge=edges.pop(0)
        parent_of_start=collapsing_find(parents,edge[1])
        parent_of_end=collapsing_find(parents,edge[2])
        if parent_of_start!=parent_of_end:
            weightingUnion(parents,childs,parent_of_start,parent_of_end)
            MST.append(edge)
            total_weight+=edge[0]
            vertices.append(edge[1])
            vertices.append(edge[2])
    return MST,total_weight


if __name__ == "__main__":
    print(kruskal(mygraph))
