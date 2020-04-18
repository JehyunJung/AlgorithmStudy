import heapq
from math import sqrt

def get_distance(pos1,pos2):
    return sqrt((pos2[0]-pos1[0])**2+(pos1[1]-pos2[1])**2)

def collapsing_find(p,parents):
    if parents[p]!=p:
        parents[p]=collapsing_find(parents[p],parents)
    return parents[p]

def union(m,n,parent,childs):
    if childs[m]>=childs[n]:
        parent[n]=m
        childs[m]+=childs[n]
        if childs[n]==0:
            childs[m]+=1

    else:
        parent[m]=n
        childs[n]+=childs[m]
        if childs[m]==0:
            childs[n]+=1

def solution():
    n_vertex,n_edges=map(int,input().split(' '))
    vertices=[None,]
    edges=[]
    parents=[vertex for vertex in range(n_vertex+1)]
    childs=[0 for vertex in range(n_vertex+1)]
    for _ in range(n_vertex):
        row,col=map(int,input().split(' '))
        vertices.append((row,col))

    for x in range(1,n_vertex):
        for y in range(x+1,n_vertex+1):
            edges.append((x,y,get_distance(vertices[x],vertices[y])))

    edges.sort(key=lambda x:x[2])
    for _ in range(n_edges):
        start,end=map(int,input().split(' '))
        parent_start,parent_end=collapsing_find(start,parents),collapsing_find(end,parents)
        union(parent_start,parent_end,parents,childs)

    result=0
    for start,end,weight in edges:
        parent_start,parent_end=collapsing_find(start,parents),collapsing_find(end,parents)
        if parent_start!=parent_end:
            union(parent_start,parent_end,parents,childs)
            result+=weight

    print('%0.2f' % result)

if __name__=="__main__":
    solution()