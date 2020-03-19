data_num=int(input())
data_set=set(map(int,input().split(' ')))
search_num=int(input())
search_set=list(map(int,input().split(' ')))
for data in search_set:
    if data in data_set:
        print('1')
    else:
        print('0')