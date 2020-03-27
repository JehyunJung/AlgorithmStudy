import sys
def quickSort(data):
    if len(data)<=1:
        return data
    pivot=data[0]
    left_data=[element for element in data[1:] if element < pivot]
    right_data=[element for element in data[1:] if element >= pivot]

    return quickSort(left_data) + [pivot] + quickSort(right_data)

def solution():
    num=int(sys.stdin.readline())
    data_countings=[0]*10001
    for _ in range(num):
        data=int(sys.stdin.readline())
        data_countings[data]+=1
    for index in range(len(data_countings)):
        for _ in range(data_countings[index]):
            print(index)


if __name__ == "__main__":
    solution()
