def bubbleSort(data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
    return data

def quickSort(data):
    if len(data)==0:
        return data

    pivot=data[0]
    left_data=[]
    right_data=[]
    equal_data=[]
    for element in data:
        if element < pivot:
            left_data.append(element)
        elif element > pivot:
            right_data.append(element)
        else:
            equal_data.append(element)
    return quickSort(left_data) + equal_data + quickSort(right_data)



def merge(left_data,right_data):
    merged=[]
    i,j=0,0
    while i <len(left_data) and j < len(right_data):
        if left_data[i] < right_data[j]:
            merged.append(left_data[i])
            i+=1
        else:
            merged.append(right_data[j])
            j+=1
    if i == len(left_data):
        for j in range(j, len(right_data)):
            merged.append(right_data[i])
    else:
        for i in range(i,len(left_data)):
            merged.append(left_data[i])

    return merged

def mergeSort(data):
    if len(data)<=1:
        return data
    medium=len(data)//2
    left_data=mergeSort(data[:medium])
    right_data=mergeSort(data[medium:])
    return merge(left_data,right_data)

def solution():
    num=int(input())
    inputs=[]
    for _ in range(num):
        inputs.append(int(input()))
    inputs.sort()
    for item in inputs:
        print(item)

if __name__=="__main__":
    solution()