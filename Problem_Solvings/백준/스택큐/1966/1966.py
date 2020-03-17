def solution(test_cases):
    for _ in range(test_cases):
        count=0
        queue=[]
        doc_num,track_doc=list(map(int,input().split(' ')))
        priorities=list(map(int,input().split(' ')))
        for doc in range(doc_num):
            queue.append(doc)

        while len(queue) !=0:
            if max(priorities) > priorities[queue[0]]:
                queue.append(queue.pop(0))
            elif max(priorities) == priorities[queue[0]]:
                count+=1
                item=queue.pop(0)
                priorities[item]=-1
                if item==track_doc:
                    print(count)
                    break

if __name__ == "__main__":
    test_cases=int(input())
    solution(test_cases)