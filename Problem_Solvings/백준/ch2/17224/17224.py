def solution():
    n_questions,skill, answer_limit=map(int,input().split())
    easy=0
    hard=0

    for _ in range(n_questions):
        sub1,sub2=map(int,input().split(' '))
        if sub1<=skill:
            easy+=1
        if sub2<=skill:
            hard+=1
    score=min(hard,answer_limit)*140

    if hard<answer_limit:
        score+=min(easy-hard,answer_limit-hard)*100

    print(score)

if __name__=="__main__":
    solution()