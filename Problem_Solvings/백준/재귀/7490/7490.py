def solution(array,current,n):
    if current==n:
        expression=('').join(array)
        expression+=str(n)

        if eval(expression.replace(' ',''))==0:
            print(expression)
        return

    solution(array+[str(current)]+[' '],current+1,n)
    solution(array+[str(current)]+['+'],current+1,n)
    solution(array+[str(current)]+['-'],current+1,n)

if __name__ =="__main__":
    test_cases=int(input())
    for _ in range(test_cases):
        solution([],1,int(input()))
        print()