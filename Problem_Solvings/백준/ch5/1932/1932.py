def dfs(index,count,trace):
    global result
    if count==depth:
        result=max(result,sum(trace))
        return

    dfs(index+count,count+1,trace+[numbers[index+count]])
    dfs(index+count+1,count+1,trace+[numbers[index+count+1]])
    return

result=0
depth=int(input())
numbers=[None]
for _ in range(depth):
    numbers.extend(list(map(int,input().split(' '))))

dfs(1,1,[numbers[1]])
print(result)