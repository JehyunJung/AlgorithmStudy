def pour(amount,capacity,index):
    next_index=(index+1)%3
    if amount[index]+amount[next_index]<=capacity[next_index]:
        amount[next_index]+=amount[index]
        amount[index]=0
    else:
        amount[index]-=(capacity[next_index]-amount[next_index])
        amount[next_index]=capacity[next_index]

def solution():
    capacity=[]
    amount=[]

    for _ in range(3):
        value1,value2=map(int,input().split(' '))
        capacity.append(value1)
        amount.append(value2)

    for index in range(100):
        pour(amount,capacity,index%3)

    for value in amount:
        print(value)
if __name__ == "__main__":
    solution()
