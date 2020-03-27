def solution():
    coordinates_num, antenna_num=list(map(int,input().split(' ')))
    coordinates=[]
    for _ in range(coordinates_num):
        coordinates.append(int(input()))

    coordinates.sort()
    start=coordinates[1]-coordinates[0]
    end=coordinates[-1]-coordinates[0]
    result=0
    while start <= end:
        med=(start+end)//2
        count=1
        starting_point=coordinates[0]
        for i in range(1,len(coordinates)):
            if coordinates[i]>=starting_point+med:
                count+=1
                starting_point=coordinates[i]
        if count>=antenna_num:
            start=med+1
            result=med
        else :
            end=med-1
    print(result)

if __name__ == "__main__":
    solution()