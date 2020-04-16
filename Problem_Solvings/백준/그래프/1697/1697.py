from collections import deque
def solution():
    start_point,end_point=map(int,input().split(' '))
    level=[0]*100001

    queue=deque([start_point])
    while queue:
        point=queue.popleft()
        if point == end_point:
            break

        for next_pos in (point-1,point+1,2*point):
            if 0<=next_pos<=100000 and level[next_pos] == 0:
                level[next_pos]=level[point]+1
                queue.append(next_pos)

    print(level[end_point])

if __name__ == "__main__":
    solution()