def solution():
    n_rows,n_cols=list(map(int,input().split(' ')))
    guards=[]
    required_cols=list(range(n_cols))
    required_rows=list(range(n_rows))

    guard_col=set()
    guard_row=set()
    for row in range(n_rows):
        data=input()
        for index in range(len(data)):
            if data[index]!='.':
                guard_col.add(index)
                guard_row.add(row)
    required_cols=set(required_cols)
    required_rows=set(required_rows)

    print(max(len(required_cols-guard_col),len(required_rows-guard_row)))

if __name__=="__main__":
    solution()