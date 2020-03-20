def solution(test_cases):
    for _ in range(test_cases):
        leftstack=[]
        rightstack=[]
        password=input()
        for character in password:
            if character == '<':
                if leftstack:
                    rightstack.append(leftstack.pop())
            elif character =='>':
                if rightstack:
                    leftstack.append(rightstack.pop())
            elif character =='-':
                if leftstack:
                    leftstack.pop()
            elif character not in ['<','>','-']:
                leftstack.append(character)
        leftstack.extend(reversed(rightstack))
        print(''.join(leftstack))

if __name__ =="__main__":
    test_cases=int(input())
    solution(test_cases)