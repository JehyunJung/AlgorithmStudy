def fibo_1(num):
    if num<=0:
        return 0
    elif num==1:
        return 1
    else:
        return fibo_1(num-1)+fibo_1(num-2)
def fibo_2(num):
    fibo_data=[0,1]
    for index in range(2,num+1):
        fibo_data.append(fibo_data[index-1]+fibo_data[index-2])
    return fibo_data[num]

def solution():
    print(fibo_2(int(input())))

if __name__ =="__main__":
    solution()
