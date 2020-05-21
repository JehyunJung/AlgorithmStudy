import re
def solution():
    strings=input()
    reversed_string=""
    splitted=re.split('(\<[\w\s]+\>)',strings)
    for string in splitted:
        if string=="":
            continue
        if '<' in string:
            print(string,end="")
        else:
            space_splitted=string.split(' ')
            print(space_splitted[0][-1::-1],end="")
            for segment in space_splitted[1:]:
                print(" "+segment[-1::-1],end="")

if __name__ == "__main__":
    solution()