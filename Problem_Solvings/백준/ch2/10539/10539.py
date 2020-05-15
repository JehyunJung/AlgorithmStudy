def solution():
    n_inputs=input()
    inputs=list(map(int,input().split(' ')))

    a_sum=0
    for b_index, b_value in enumerate(inputs):
        temp_value=b_value*(b_index+1)-a_sum
        print(temp_value,end=" ")
        a_sum+=temp_value

if __name__ == "__main__":
    solution()