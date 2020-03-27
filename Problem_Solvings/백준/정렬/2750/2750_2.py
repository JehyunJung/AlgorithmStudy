def solution():
    num=int(input())
    sort_data=[]
    for count in range(0,num):
        sort_data.append(int(input()))

    sort_data.sort()

    for data in sort_data:
        print(data)


if __name__ == "__main__":
    solution()