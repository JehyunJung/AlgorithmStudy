from itertools import combinations
def decoder():
    for code in combinations(choices,length):
        vow_count=0
        for element in code:
            if element in vowels:
                vow_count+=1
        if length-vow_count>=2 and vow_count>=1:
            print(''.join(code))


length,types=map(int,input().split(' '))
choices=list(input().split(' '))
choices.sort()
vowels=['a','e','i','o','u']

decoder()



