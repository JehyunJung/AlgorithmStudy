from operator import itemgetter
def quickSort(data):
    if len(data)<=1:
        return data
    pivot=data[0]
    left_data=[]
    right_data=[]
    equal_data=[]
    for element in data:
        if element[0]<pivot[0]:
            left_data.append(element)
        elif element[0]==pivot[0]:
            if element[1]<pivot[1]:
                left_data.append(element)
            elif element[1]==pivot[1]:
                equal_data.append(element)
            else:
                right_data.append(element)
        else:
            right_data.append(element)

    return quickSort(left_data) + equal_data + quickSort(right_data)

def solution():
    num=int(input())
    data=[]
    for _ in range(num):
        xpos,ypos=list(map(int, input().split(' ')))
        data.append((xpos,ypos))

    #sorted_data=quickSort(data)
    sorted_data=sorted(data,key=itemgetter(0,1))

    for element in sorted_data:
        print(element[0],element[1])

if __name__ == "__main__":
    solution()
