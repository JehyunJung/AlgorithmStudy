def solution(space,xpos,ypos):
    space_count=2**space
    space_count*=space_count

    current_xside=(0,2**space-1)
    current_yside=(0,2**space-1)
    count=0
    while True:
        med_y=(current_yside[0]+current_yside[1])//2
        med_x=(current_xside[0]+current_xside[1])//2

        if ypos > med_y and ypos <=current_yside[1]:
            count+=space_count//2
            current_yside=(med_y+1,current_yside[1])
        else:
            current_yside=(current_yside[0],med_y)

        if xpos > med_x and xpos <=current_xside[1]:
            count+=space_count//4
            current_xside=(med_x+1,current_xside[1])
        else:
            current_xside=(current_xside[0],med_x)

        if current_yside[0]==ypos and current_xside[0]==xpos:
            break

        space_count//=4

    print(count)

if __name__ == "__main__":
    space,y_pos,x_pos=list(map(int, input().split(' ')))
    solution(space,x_pos,y_pos)