def solution():
    n_inputs=int(input())
    inputs=list(map(int,input().split(' ')))

    min_score,max_score=100,0

    for score in inputs:
        if score<min_score:
            min_score=score
        if score>max_score:
            max_score=score
    print(max_score-min_score)
if __name__ == "__main__":
    solution()