import heapq
class Heap:
    def __init__(self):
        self.heap=[None]
        self.heapSize=0
    def siftdown(self,index):
        parent=index
        child=parent*2
        key=self.heap[parent]
        while child <=self.heapSize:
            largerChild=child
            if child< self.heapSize and self.heap[child] >= self.heap[child+1]:
                largerChild=child+1
            if self.heap[largerChild] > self.heap[parent]:
                break
            self.heap[parent]=self.heap[largerChild]
            parent=largerChild
            child=parent*2

        self.heap[parent]=key

    def pop(self):
        data=self.heap[1]
        self.heap[1]=self.heap[-1]
        del self.heap[-1]
        self.heapSize-=1
        if self.heapSize!=0:
            self.siftdown(1)
        return data

    def push(self,data):
        self.heap.append(data)
        self.heapSize+=1

        child=self.heapSize
        parent=child//2

        while child !=1 and self.heap[parent] > data:
            self.heap[child]=self.heap[parent]
            child=parent
            parent/=2
        self.heap[child]=data

    def makeHeap(self):
        for i in range(self.heapSize//2,1):
            self.siftdown(self,i)

    def isEmpty(self):
        return True if self.heapSize ==0  else False


def solution():
    n_times=int(input())
    heap=Heap()
    for _ in range(n_times):
        key=int(input())

        if key==0:
            if heap.isEmpty():
                print(0)
            else:
                print(heap.pop())
        else:
            heap.push(key)
    # heap=[]
    # for _ in range(n_times):
    #     key=int(input())
    #
    #     if key==0:
    #         if heap:
    #             print(heapq.heappop(heap))
    #         else:
    #             print(0)
    #     else:
    #         heapq.heappush(heap,key)

if __name__ =="__main__":
    solution()