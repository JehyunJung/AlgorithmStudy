def solution(num):
    stack=[]
    result=[]
    count=1
    for _ in range(1,num+1):
        data=int(input())
        while count<=data:
            stack.append(count)
            count+=1
            result.append('+')
        if data == stack[-1]:
            stack.pop()
            result.append('-')
        else:
            print('NO')
            return

    print(('\n').join(result))

if __name__ =="__main__":
    num=int(input())
    solution(num)
