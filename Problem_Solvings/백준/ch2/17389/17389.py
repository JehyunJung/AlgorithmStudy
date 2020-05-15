def solution():
    input_num=int(input())
    answer_sheet=input()
    bonus=0
    score=0
    for index,answer in enumerate(answer_sheet):
        if ord(answer)==79:
            score+=(index+1)+bonus
            bonus+=1
        else:
            bonus=0
    print(score)
if __name__=="__main__":
    solution()