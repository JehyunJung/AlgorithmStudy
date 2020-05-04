def promising(queens,new_column):
    current_row=len(queens)
    for row in range(current_row):
        if queens[row]==new_column or current_row-row==abs(new_column-queens[row]):
            return False
    return True

def n_queens(num,queens,count):
    if len(queens)==num:
        count[0]+=1

    for i in range(num):
        if promising(queens,i):
           n_queens(num,queens+[i],count)


def solution():
    num=int(input())
    count=[0]
    n_queens(num,[],count)
    print(count[0])
if __name__ == "__main__":
    solution()