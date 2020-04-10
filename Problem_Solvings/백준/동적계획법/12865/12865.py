def solution():
    n_items,remaining_weight=map(int,input().split(' '))
    bag=[[0]*(remaining_weight+1) for _ in range(n_items+1)]

    for index in range(1,n_items+1):
       weight,priority=map(int,input().split(' '))
       for max_limit in range(remaining_weight+1):
           if max_limit >= weight:
               bag[index][max_limit]=max(bag[index-1][max_limit],bag[index-1][max_limit-weight]+priority)
           else:
               bag[index][max_limit]=bag[index-1][max_limit]
    print(bag[n_items][remaining_weight])



if __name__=="__main__":
    solution()