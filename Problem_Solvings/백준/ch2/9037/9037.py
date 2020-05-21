def check(array):
    return len(set(array))==1

def solution():
    n_testcases=int(input())
    for _ in range(n_testcases):
        rotation_count=0
        n_childs=int(input())
        child_candies=list(map(int,input().split(' ')))
        if n_childs==1:
            print(0)
            continue

        for index in range(n_childs):
            if child_candies[index]%2!=0:
                child_candies[index]+=1

        while True:
            if check(child_candies):
                break
            prev_candy=child_candies[-1]
            for index in range(0,n_childs):
                child_candies[index],prev_candy=child_candies[index]+prev_candy//2-child_candies[index]//2,child_candies[index]
                if child_candies[index]%2!=0:
                    child_candies[index]+=1
            rotation_count+=1

        print(rotation_count)

if __name__ == "__main__":
    solution()