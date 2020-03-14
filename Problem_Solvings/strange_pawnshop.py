
def cost(data):
    print(data)
    return min(data)*max(data)*len(data)

def combinations(data,length):
    combs=list()
    for i in range(len(data)-length+1):
        comb=list()
        for j in range(0,length):
            comb.append(data[i+j])
        combs.append(comb)
    return combs

def solution():
    numbers=list()
    n=int(input())
    for i in range(n):
        numbers.append(int(input()))
    sum=0
    for i in range(1,len(numbers)+1):
        sub_numbers=combinations(numbers,i)
        for j in sub_numbers:
            sum+=cost(j)
    return sum

if __name__ == "__main__":
    print(solution())
