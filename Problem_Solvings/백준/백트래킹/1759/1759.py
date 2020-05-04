def promising(code):
    con_count,vow_count=0,0

    for element in code:
        if element in consonants:
            con_count+=1
        elif element in vowels:
            vow_count+=1

    if con_count>=2 and vow_count>=1:
        return True

def decoder(code,index):
    if len(code)==length and promising(code):
        print(code)
        return

    while index< types:
        decoder(code+choices[index],index+1)
        index+=1


length,types=map(int,input().split(' '))
choices=list(input().split(' '))
choices.sort()
consonants=[]
vowels=[]

for choice in choices:
    if choice in ['a','e','i','o','u']:
        vowels.append(choice)
    else:
        consonants.append(choice)

decoder('',0)



