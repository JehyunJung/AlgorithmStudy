def solution():
    group_num,question_num=map(int,input().split(' '))
    groups={}
    for _ in range(group_num):
        group_name=input()
        groups[group_name]=[]
        member_num=int(input())
        for _ in range(member_num):
            groups[group_name].append(input())

    for _ in range(question_num):
        question=input()
        question_type=int(input())
        if question_type== 0:
            print("\n".join(sorted(groups[question])))
        else:
            for group_name in groups.keys():
                if question in groups[group_name]:
                    print(group_name)
                    break


if __name__ =="__main__":
    solution()