from random import *
class Heap:
    def __init__(self,data):
        self.heap=list()
        self.heap.append(None)
        self.heap.append(data)
        self.heapSize=1

    def insert(self,data):
        self.heapSize+=1
        child=self.heapSize
        self.heap.append(data)
        parent=child//2
        while(parent>=1 and data > self.heap[parent]):
            self.heap[child]=self.heap[parent]
            child=parent
            parent=child//2
        self.heap[child]=data

    def siftdown(self,index):
        parent=index
        key=self.heap[index]
        while(parent*2 <= self.heapSize):
            largerChild=parent*2
            if parent*2 < self.heapSize and self.heap[parent*2] < self.heap[parent*2+1]:
                largerChild=parent*2+1
            if self.heap[parent]>self.heap[largerChild]:
                break
            self.heap[parent]=self.heap[largerChild]
            parent=largerChild
        self.heap[parent]=key

    def delete(self):
        item=self.heap[1]
        self.heap[1]=self.heap[self.heapSize]
        self.heapSize-=1
        self.siftdown(1)
        del self.heap[self.heapSize+1]
        return item

    def makeHeap(self,data):
        for i in range(self.heapSize//2,0,-1):
            self.siftdown(i)
def main():
    heap=Heap(1)
    for i in range(0,10):
        item=randint(0,100)
        heap.insert(item)
        print("{}. inserted item {} heapSize: {}".format(i,item,heap.heapSize))
    print(heap.heap)
    print('deleted item:',heap.delete())
    print(heap.heap)
if __name__ == "__main__" :
    main()