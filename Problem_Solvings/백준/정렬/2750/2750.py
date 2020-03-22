def solution(num):
    sort_data=[]
    for count in range(0,num):
        data=int(input())
        sort_data.append(data)


        key=sort_data[count]
        sorted_index=count-1

        while sorted_index >=0:
            if key < sort_data[sorted_index]:
                sort_data[sorted_index+1]=sort_data[sorted_index]
                sorted_index-=1
            else:
                break
        sort_data[sorted_index+1]=key

    for data in sort_data:
        print(data)


if __name__ == "__main__":
    solution(int(input()))