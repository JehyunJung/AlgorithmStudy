def height_checker(data):
    max=data[0]
    count=1
    for trophy in data:
        if max<trophy:
            count+=1
            max=trophy
    print(count)

def solution():
    num=int(input())
    trophies=[]
    for _ in range(num):
        trophies.append(int(input()))
    height_checker(trophies)
    trophies.reverse()
    height_checker(trophies)

if __name__ == "__main__":
    solution()