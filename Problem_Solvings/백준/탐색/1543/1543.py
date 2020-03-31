import re
def solution():
    data=input()
    pattern=input()

    count=0
    i=0
    while i <= len(data)-len(pattern):
        if data[i:i+len(pattern)]==pattern:
            count+=1
            i+=len(pattern)
        else:
            i+=1
    print(count)

def solution_2():
    data=input()
    print(len(re.findall(input(),data)))
if __name__ == "__main__":
    #solution()
    solution_2()