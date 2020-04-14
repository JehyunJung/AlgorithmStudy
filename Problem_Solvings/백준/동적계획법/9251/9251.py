def solution():
    string1=input()
    string2=input()

    x=len(string1)
    y=len(string2)
    LCS=[[0]*(y+1) for _ in range(x+1)]

    for i in range(1,x+1):
        for j in range(1,y+1):
            if string1[i-1]==string2[j-1]:
                LCS[i][j]=LCS[i-1][j-1]+1
            else:
                LCS[i][j]=max(LCS[i-1][j],LCS[i][j-1])
    print(LCS[x][y])
if __name__=="__main__":
    solution()