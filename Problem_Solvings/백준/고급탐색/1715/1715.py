import heapq
def solution():
    n=int(input())
    array=[]
    for _ in range(n):
        heapq.heappush(array,int(input()))
    sum=0
    while len(array)>1:
        data=heapq.heappop(array)+heapq.heappop(array)
        sum+=data
        heapq.heappush(array,data)

    print(sum)
if __name__ == "__main__":
    solution()