def solution():
    n_inputs=int(input())
    data=list(map(int,input().split(' ')))

    asc_count=[0]*n_inputs

    for index in range(0,n_inputs):
        max_asc=0
        for target_index in range(index-1,-1,-1):
            if data[index]>data[target_index]:
                max_asc=max(max_asc,asc_count[target_index])
        asc_count[index]=max_asc+1

    print(max(asc_count))

if __name__=="__main__":
    solution()