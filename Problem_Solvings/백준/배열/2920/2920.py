import sys
def solution():
    data=list(map(int,input().split(' ')))
    ascending=True
    descending=True

    for i in range(len(data)-1):
        if data[i]<=data[i+1]:
            descending=False
        elif data[i]>=data[i+1]:
            ascending=False
        else:
            break

    if ascending==True:
        print('ascending')
    elif descending==True:
        print('descending')
    else:
        print('mixed')

if __name__ == "__main__":
    solution()