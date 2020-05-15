def solution():
    input_num1,input_num2=map(int,input().split(' '))
    inputs1,inputs2=input().split()
    max_index=min(input_num1,input_num2)
    name_matching= ''
    name_map=[3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

    for index in range(max_index):
        name_matching+=inputs1[index]+inputs2[index]

    name_matching+=inputs1[max_index:]+inputs2[max_index:]
    name_matching=[name_map[ord(char_value)-ord('A')] for char_value in name_matching]

    for index in range(input_num1+input_num2-2):
        temp=[]
        for index in range(input_num1+input_num2-index-1):
            temp_value=name_matching[index]+name_matching[index+1]
            temp.append(temp_value)
        name_matching=temp

    print("{}%".format(name_matching[0]%10*10+name_matching[1]%10))

if __name__ == "__main__":
    solution()