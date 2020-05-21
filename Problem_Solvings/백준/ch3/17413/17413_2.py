def solution():
    string=input()
    segment,answer="",""
    tag_open=False

    for ch in string:
        if ch ==' ':
            if tag_open:
                answer+=" "
            else:
                answer+=segment[::-1]+" "
                segment=""
        elif ch in '<':
            tag_open=True
            answer+=segment[::-1]+"<"
            segment=""
        elif ch in '>':
            tag_open=False
            answer+=">"
        else:
            if tag_open:
                answer+=ch
            else:
                segment+=ch
    answer+=segment[::-1]
    print(answer)
if __name__=="__main__":
    solution()