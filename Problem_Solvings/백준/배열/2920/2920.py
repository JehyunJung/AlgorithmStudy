import sys
def solution(source):
    ascending=True
    descending=True

    for i in range(len(source)-1):
        if source[i]<=source[i+1]:
            descending=False
        elif source[i]>=source[i+1]:
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
    data=list(map(int,input().split(' ')))
    solution(data)