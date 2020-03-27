def evaluator(array,current,n):
    if current==n:
        expression=('').join(array)
        expression+=str(n)

        if eval(expression.replace(' ',''))==0:
            print(expression)
        return

    evaluator(array+[str(current)]+[' '],current+1,n)
    evaluator(array+[str(current)]+['+'],current+1,n)
    evaluator(array+[str(current)]+['-'],current+1,n)

def solution():
    test_cases=int(input())
    for _ in range(test_cases):
        evaluator([],1,int(input()))
        print()

if __name__ =="__main__":
    solution()