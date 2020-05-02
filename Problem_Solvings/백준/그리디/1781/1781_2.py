import heapq
def solution():
    n_elements=int(input())
    elements=[]
    for _ in range(n_elements):
        deadline,value=map(int,input().split(' '))
        elements.append((deadline,value))

    elements.sort()
    heap=[]
    for deadline, value in elements:
        heapq.heappush(heap,value)

        if deadline<len(heap):
            heapq.heappop(heap)

    print(sum(heap))

if __name__=="__main__":
    solution()