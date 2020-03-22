from operator import itemgetter
def quickSort(data):
    if len(data)<=1:
        return data
    pivot=data[0]
    left_data=[element for element in data[1:] if element[0] <pivot[0]]
    right_data=[element for element in data[1:] if element[0] >=pivot[0]]

    return quickSort(left_data) + [pivot] + quickSort(right_data)

def partition(data,low,high):
    if low<high:
        key=data[low][0]
        i=low
        j=low+1
        while j<=high:
            if data[j][0]<key:
                i+=1
                data[j],data[i]=data[i],data[j]
            j+=1
        data[i],data[low]=data[low],data[i]
        return i

def quickSort_2(data,low,high):
    if(low<high):
        pivot=partition(data,low,high)
        quickSort_2(data,low,pivot-1)
        quickSort_2(data,pivot+1,high)

    return data
def quickSort_3(data):
    if len(data)<=1:
        return data
    med=len(data)//2
    pivot=data[med]
    left=[]
    right=[]
    equal=[]

    for data in data:
        if data[0]<pivot[0]:
            left.append(data)

        elif data[0]>pivot[0]:
            right.append(data)

        else:
            equal.append(data)
    return quickSort(left) + equal + quickSort(right)

def solution(data):
    #sorted_data=quickSort(data)
    #sorted_data=quickSort_2(data,0,len(data)-1)
    sorted_data=quickSort_3(data)
    for element in sorted_data:
        print(element[0],element[1])

if __name__ == "__main__":
    num=int(input())
    data=[]
    for _ in range(num):
        age,name=input().split(' ')
        data.append((int(age),name))
    solution(data)
