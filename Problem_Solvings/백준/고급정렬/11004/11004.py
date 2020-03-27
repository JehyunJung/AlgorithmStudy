import random
def partition(data):
    pivot=random.randint(0,len(data)-1)
    print(pivot)
    left_data=[]
    right_data=[]
    for index in range(len(data)):
        if index==pivot:
            continue
        if data[index]<data[pivot]:
            left_data.append(data[index])
        else:
            right_data.append(data[index])
    return left_data+[data[pivot]]+right_data, len(left_data)+1

def k_location(data,k):
    if len(data) == 1:
        return data[0]
    data,pivot=partition(data)
    if pivot == k:
        return data[pivot-1]
    elif pivot > k:
        return k_location(data[:pivot-1],k)
    else:
        return k_location(data[pivot:],k-pivot)

def solution(data,k):
    print(k_location(data,k))

if __name__ == "__main__":
    num,k_th=list(map(int,input().split(' ')))
    inputs=list(map(int,input().split(' ')))
    solution(inputs,k_th)
