import sys
def priceCalculator(flower_pos):
    dx=[0,-1,0,1,0]
    dy=[0,0,1,0,-1]


    flower_points=[]
    flowers=[]
    price=0

    for flower in flower_pos:
        x=flower // garden_size
        y=flower % garden_size
        if 0==x or x==garden_size-1 or 0==y or y==garden_size-1:
            return 3000
        for dir in range(5):
            flower_points.append((x+dx[dir],y+dy[dir]))
            price+=garden[x+dx[dir]][y+dy[dir]]
        flowers.append((x,y))
    if len(set(flower_points)) != 15:
        return 3000
    else:
        return price

def solution():
    global garden_size
    garden_size=int(input())
    global garden
    garden=[list(map(int,input().split(' '))) for _ in range(garden_size)]
    result=3000

    for i in range(garden_size+1,garden_size*garden_size-(garden_size+1)):
        for j in range(i+1,garden_size*garden_size-(garden_size+1)):
            for k in range(j+1,garden_size*garden_size-(garden_size+1)):
                result=min(result,priceCalculator([i,j,k]))

    print(result)

if __name__=="__main__":
    solution()

