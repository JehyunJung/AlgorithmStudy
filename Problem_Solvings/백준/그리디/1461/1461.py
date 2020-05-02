def solution():
    n_books,book_limit=map(int,input().split(' '))
    positive=[]
    negative=[]
    max_distance=0
    distances=list(map(int,input().split(' ')))

    for distance in distances:
        if distance <0:
            negative.append(-distance)
        else:
            positive.append(distance)
        max_distance=max(abs(distance),max_distance)

    negative.sort(reverse=True)
    positive.sort(reverse=True)

    index=0
    result=0

    while index<len(negative):
        result+=negative[index]
        for _ in range(book_limit):
            index+=1
            if index==len(negative):
                break

    index=0
    while index<len(positive):
        result+=positive[index]
        for _ in range(book_limit):
            index+=1
            if index==len(positive):
                break

    result*=2
    print(result-max_distance)

if __name__ == "__main__":
    solution()