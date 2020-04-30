def solution():
    data=input()
    zero_count,one_count=0,0
    prev_value=None
    for index in range(len(data)):
        if index>=1:
            prev_value=data[index-1]
        if prev_value !='0' and data[index]=='0':
            zero_count+=1
        elif prev_value !='1' and data[index]=='1':
            one_count+=1
    print(min(zero_count,one_count))
    
if __name__ == "__main__":
    solution()