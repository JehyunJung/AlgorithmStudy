from itertools import permutations
def rotate(matrix,permutation):
    prev_state=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            prev_state[i][j]=matrix[i][j]

    for rotation in permutation:
        r,c,s=rotation[0],rotation[1],rotation[2]
        index=0
        for _ in range(s):
            N=prev_state[r-s-1+index][c-s-1+index:c+s-1-index]
            S=prev_state[r+s-1-index][c+s-1-index:c-s-1+index:-1]
            W=[]
            E=[]
            for i in range(r-s-1+index,r+s-1-index):
                W.append(prev_state[i][c+s-1-index])
            for i in range(r+s-1-index,r-s-1+index,-1):
                E.append(prev_state[i][c-s-1+index])

            i,j=r-s-1+index,c-s+index
            for data in N:
                prev_state[i][j]=data
                j+=1
            i+=1
            j-=1
            for data in W:
                prev_state[i][j]=data
                i+=1
            j-=1
            i-=1
            for data in S:
                prev_state[i][j]=data
                j-=1
            i-=1
            j+=1
            for data in E:
                prev_state[i][j]=data
                i-=1
            index+=1
    return prev_state

def solution():
    N,M,K=map(int,input().split(' '))
    matrix=[]
    result=9999999
    for _ in range(N):
        matrix.append(list(map(int,input().split(' '))))

    rotations=[]
    for _ in range(K):
        rotations.append(list(map(int,input().split(' '))))

    for permutation in permutations(rotations):
        copy_matrix=rotate(matrix,permutation)
        min_sum=999999
        for row in range(len(matrix)):
            min_sum=min(min_sum,sum(copy_matrix[row]))
        result=min(result,min_sum)
    print(result)

if __name__=="__main__":
    solution()