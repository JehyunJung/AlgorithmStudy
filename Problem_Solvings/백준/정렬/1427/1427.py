def bubbleSort(data):
    for i in range(len(data)):
        swap=False
        for j in range(len(data)-i-1):
            if data[j]<data[j+1]:
                data[j+1],data[j]=data[j],data[j+1]
                swap=True
        if swap==False:
            break
    return data

def quickSort(data):
    if len(data)<=1:
        return data
    pivot=data[0]
    left_data=[element for element in data[1:] if element >pivot]
    right_data=[element for element in data[1:] if element <=pivot]

    return quickSort(left_data) + [pivot] + quickSort(right_data)

def merge(data1,data2):
    merged_data=[]
    i,j=0,0
    while i < len(data1) and j < len(data2):
        if data1[i]<data2[j]:
            merged_data.append(data1[i])
            i+=1
        else:
            merged_data.append(data2[j])
            j+=1

    for i in range(i,len(data1)):
        merged_data.append(data1[i])
    for j in range(j, len(data2)):
        merged_data.append(data2[j])

    return merged_data

def mergeSort(data):
    if len(data)<=1:
        return data
    medium=len(data)//2

    left_data= mergeSort(data[:medium])
    right_data=mergeSort(data[medium:])

    return merge(left_data,right_data)


def solution_2():
    string=input()
    for count in range(9,-1,-1):
        for element in string:
            if int(element)==count:
                print(element,end='')

def solution():
    string=input()
    sort_data=[int(char) for char in string]
    sort_data=mergeSort(sort_data)
    for data in sort_data:
        print(data,end='')

if __name__ == "__main__":
    solution()
    #solution_2()