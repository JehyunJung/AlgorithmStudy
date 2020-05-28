import copy
def dfs(graph,count): #전수조사를 진행할 dfs
    result=max([max(i) for i in graph])
    if count==0: # 5번의 움직임 이후에는 재귀 종료
        return result
    for _ in range(4):
        moved_graph=movement(graph)
        if moved_graph != graph:
            result=max(result,dfs(moved_graph,count-1))
        graph=rotate(graph)
    return result

def rotate(graph):
    new_graph=[[0 for _ in range(graph_size)] for _ in range(graph_size)]
    for i in range(graph_size):
        for j in range(graph_size):
            new_graph[j][graph_size-1-i]=graph[i][j]
    return new_graph

def movement(graph): #moves 배열에 저장되어있는 움직임에 따라 그래프에 적용
    new_graph=copy.deepcopy(graph)
    for i in range(graph_size):
        tmp=[value for value in graph[i] if value >0]
        for index in range(1,len(tmp)):     #2048 규칙에 의해 이동된 숫자는 합쳐준다.
            if tmp[index]==tmp[index-1]:
                tmp[index-1]*=2
                tmp[index]=0
        tmp=[value for value in tmp if value>0]
        new_graph[i]=tmp+[0]*(graph_size-len(tmp))
    return new_graph

graph_size=int(input())
graph=[]

result=0

for _ in range(graph_size):
    graph.append(list(map(int,input().split(' '))))

print(dfs(graph,5))


